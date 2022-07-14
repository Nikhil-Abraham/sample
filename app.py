from flask import Flask, request, render_template
from requests_html import HTMLSession
import requests
import spacy
from spacy import displacy
from bs4 import BeautifulSoup

session = HTMLSession()


app = Flask(__name__)


def nre(text):

    res = []

    if 'https://www' not in text:
        data = text
    else:
        try:
            html_content = session.get(text).text
            soup = BeautifulSoup(html_content, "lxml")
            data=soup.body.text
        except:
            data = "ERROR"
            res.append('ERROR')

    NER = spacy.load("en_core_web_sm")

    text1= NER(data)



    for word in text1.ents:
        print(word.text,word.label_)
        res.append(word.text)
        res.append(word.label_)

    spacy.explain("ORG")
    spacy.explain("GPE")
    spacy.explain("PRODUCT")
    spacy.explain("LOC")
    spacy.explain("DATE")
    spacy.explain("ORDINAL")
    spacy.explain("MONEY")

    res.append(str(text1))

    return res


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
