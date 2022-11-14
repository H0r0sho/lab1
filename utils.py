import csv
import requests


file_name = "dataset.csv"


def get_previous_url(url):
    data = requests.get(url).json()
    previousurl = data['PreviousURL']
    newurl = f'https:{previousurl}'
    return newurl


def get_date (url):
    data = requests.get(url).json()
    newdate = data['Date']
    shortdate = newdate[:10]
    return shortdate


def get_value (url):
    data = requests.get(url).json()
    newvalue = (data['Valute']['USD']['Value'])
    return newvalue


def run():
    with open(file_name, "w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh, quoting=csv.QUOTE_ALL)
        writer.writerow(["Дата, Курс"])
        url = "https://www.cbr-xml-daily.ru/archive/2022/10/22/daily_json.js"
        badurl="https://www.cbr-xml-daily.ru/archive/1992/06/30/daily_json.js"
        while (url != badurl):
            value = get_value(url)
            date = get_date(url)
            writer.writerow([f'{date}, {value}'])
            newurl = get_previous_url(url)
            url = newurl


