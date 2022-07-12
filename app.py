from flask import Flask, request, render_template
from requests_html import HTMLSession
import requests
session = HTMLSession()


app = Flask(__name__)


def nre(text):

    if 'https://www' not in text:
        data = text
    else:
        x = session.get(text)
        print(x.text)
        data = x.text

    return data


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')

    if request.method == 'POST':
        data = request.form.get('test_input')
        config = nre(data)
        return render_template('home.html', result=config)


@app.route('/predict')
def predict():
    return "this is the /predict page!"


if __name__ == '__main__':
    app.run()
