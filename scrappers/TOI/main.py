import requests
from bs4 import BeautifulSoup

URL = "https://timesofindia.indiatimes.com/home/headlines"

req = requests.get(url=URL)

html_doc = req.text
soup = BeautifulSoup(html_doc, 'html.parser')
body = soup.find("body")


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
    top_news_items = body.find("div", {"class":"top-newslist"}).find("ul", {"class":"clearfix"}).find_all("li")
    print(f"TOP HEADLINES -> {len(top_news_items)}", end="\n\n")
    for item in top_news_items:
        print(item.text, end="\n\n")
    top_news_items = body.find("div", {"class":"headlines-list"}).find("ul", {"class":"clearfix"}).find_all("li")
    print("\n\n")
    print(f"HEADLINES -> {len(top_news_items)}", end="\n\n")
    for item in top_news_items:
        print(item.text, end="\n\n")



getTopHeadlines()
print("\n\n")

cities = getAllCities()
top_newslist = top_newslist_small()
headlines = headlines_list()

for index in range(len(cities)):
    print(f"{cities[index].upper()}\n\n")
    for news in top_newslist[index]:
        print(f"-> {news}")
    print("\n\n")
    for news in headlines[index]:
        print(f"-> {news}")
    print("\n\n\n\n")
    print("-" * 30)