from pprint import pprint
from bs4 import BeautifulSoup
import csv
import requests
file_name="dataset.csv"
url = "https://www.cbr-xml-daily.ru/archive/2022/10/22/daily_json.js"
data = requests.get(url).json()
date=(data['Date'])
value=(data['Valute']['USD']['Value'])
previousurl=(data['PreviousURL'])
def get_previous_url(url):
    data=requests.get(url).json()
    previousurl=(data['PreviousURL'])
    newurl=f'https:{previousurl}'
    return newurl
def get_date(url):
    data = requests.get(url).json()
    newdate=(data['Date'])
    return newdate
def get_value(url):
    data = requests.get(url).json()
    newvalue = (data['Valute']['USD']['Value'])
    return newvalue
with open(file_name, "w", encoding="utf-8", newline="") as fh:
    writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
    writer.writerow(["Дата", "Value"])
    while (url!='https://www.cbr-xml-daily.ru/archive/1992/06/30/daily_json.js'):
        value = get_value(url)
        date = get_date(url)
        writer.writerow([f'{date}, {value}'])
        newurl = get_previous_url(url)
        url = newurl
file_name.close()
