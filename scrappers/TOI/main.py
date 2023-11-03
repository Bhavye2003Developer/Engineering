import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://timesofindia.indiatimes.com/home/headlines"

req = requests.get(url=URL)

html_doc = req.text
soup = BeautifulSoup(html_doc, 'html.parser')
body = soup.find("body")



def getFileName():
    today_date = datetime.today().strftime('%Y-%m-%d')
    file_name = f"scrapped_data/{today_date}_file.txt"
    return file_name


def getAllCities():
    cities = []
    cities_text_all = body.find_all("h2", {"class":"heading2"})
    for item in cities_text_all:
        city = BeautifulSoup(str(item), "html.parser").find('a')
        cities.append(city.text)
    return cities


def top_newslist_small():
    top_newslist = []
    mtero_cities_top_newslist = body.find("div", {"class","metro-cities"}).find_all("div", {"class":"top-newslist small"})
    for news_item in mtero_cities_top_newslist:
        item = BeautifulSoup(str(news_item), "html.parser")
        news_items = item.find("ul", {"class":"cvs_wdt clearfix"}).find_all("li")
        news_list = []
        for news in news_items:
            news_list.append(news.text)
        top_newslist.append(news_list)
    return top_newslist


def headlines_list():
    headline_list = []
    mtero_cities_top_newslist = body.find("div", {"class","metro-cities"}).find_all("div", {"class":"headlines-list"})
    for news_item in mtero_cities_top_newslist:
        item = BeautifulSoup(str(news_item), "html.parser")
        news_items = item.find("ul", {"class":"cvs_wdt clearfix"}).find_all("li")
        news_list = []
        for news in news_items:
            news_list.append(news.text)
        headline_list.append(news_list)
    return headline_list


def getTopHeadlines():
    # headlines
    result = ""
    top_news_items = body.find("div", {"class":"top-newslist"}).find("ul", {"class":"clearfix"}).find_all("li")
    result+=f"TOP HEADLINES -> {len(top_news_items)}"
    result+="\n\n"
    for item in top_news_items:
        result+=item.text
        result+="\n\n"
    top_news_items = body.find("div", {"class":"headlines-list"}).find("ul", {"class":"clearfix"}).find_all("li")
    result+="\n\n"
    result+=f"HEADLINES -> {len(top_news_items)}"
    result+="\n\n"
    for item in top_news_items:
        result+=item.text
        result+="\n\n"
    return result



file = getFileName()
try:
    files = os.listdir("scrapped_data")
    print(files)
except FileNotFoundError:
    print("Folder doesn't exists")
    os.mkdir("scrapped_data")
    print("Folder created successfully")


with open(file, "a", encoding="utf-8") as fs:
    try:
        fs.write(getTopHeadlines())
        fs.write("\n\n")
        result = ""
        cities = getAllCities()
        top_newslist = top_newslist_small()
        headlines = headlines_list()

        for index in range(len(cities)):
            result+=f"{cities[index].upper()}\n\n"
            for news in top_newslist[index]:
                result+=f"-> {news}\n\n"
            for news in headlines[index]:
                result+=f"-> {news}"
            result+="\n\n"
            result+="-" * 30
            result+="\n\n\n\n"
        result = result.rstrip()
        fs.write(result)
        print("Data Scrapped successfully")

    except Exception as e:
        print("Error : {e}")
