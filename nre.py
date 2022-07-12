import spacy
from spacy import displacy
from bs4 import BeautifulSoup
import requests
import re

NER = spacy.load("en_core_web_sm")

raw_text="The Indian Space Research Organisation or is the national space agency of India, headquartered in Bengaluru. It operates under Department of Space which is directly overseen by the Prime Minister of India while Chairman of ISRO acts as executive of DOS as well."

text1= NER(raw_text)

for word in text1.ents:
    print(word.text,word.label_)

spacy.explain("ORG")
spacy.explain("GPE")
displacy.render(text1,style="ent",jupyter=True)

raw_text2='The Mars Orbiter Mission (MOM), informally known as Mangalyaan, was launched into Earth orbit on 5 November 2013 by the Indian Space Research Organisation (ISRO) and has entered Mars orbit on 24 September 2014. India thus became the first country to enter Mars orbit on its first attempt. It was completed at a record low cost of $74 million.'

text2= NER(raw_text2)

for word in text2.ents:
    print(word.text,word.label_)

spacy.explain("PRODUCT")

spacy.explain("LOC")

spacy.explain("DATE")

spacy.explain("ORDINAL")

spacy.explain("MONEY")

displacy.render(text2,style="ent",jupyter=True)

URL='https://www.google.com/search?q=named+entity+recognition+using+spacy+github&oq=&aqs=chrome.0.69i59i450l8.1555238363j0j15&sourceid=chrome&ie=UTF-8'

html_content = requests.get(URL).text

soup = BeautifulSoup(html_content, "lxml")

body=soup.body.text

text3= NER(body)

displacy.render(text3,style="ent",jupyter=True)