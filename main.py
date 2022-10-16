from pprint import pprint
from bs4 import BeautifulSoup
import requests
import os
import time
import document
url = "https://www.cbr-xml-daily.ru/archive/2000/09/06/daily_json.js"
response = requests.get(url, verify=False)
print(response.text)
soup = BeautifulSoup(response.text, "lxml")


data = requests.get(url).json()
pprint(data['PreviousURL'])
pprint(data['Valute']['USD']['Value'])
url=(data['PreviousURL'])
print(url)