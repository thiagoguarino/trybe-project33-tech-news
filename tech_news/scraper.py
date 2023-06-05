import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
from .database import create_news

# file authorship: thiago guarino


# Task 1
def fetch(url):
    """
        makes a HTTP Request to a URL and gets its content
    """
    headers = {"user-agent": "Fake user-agent"}

    time.sleep(1)

    try:
        response = requests.get(url, headers, timeout=3)

        if response.status_code == 200:
            return response.text
    except requests.Timeout:
        return None


# Task 2
def scrape_updates(html_content):
    """
        scrape Trybe's main News Page to obtain a list of URL links to Articles
    """
    selector = Selector(html_content)
    news_url_list = selector.css(".entry-title a::attr(href)").getall()

    if not news_url_list:
        return []

    return news_url_list


# Task 3
def scrape_next_page_link(html_content):
    """
        scrape Trybe's main News Page to obtain a URL link to next news page
    """
    selector = Selector(html_content)
    next_page_url = selector.css("a.next::attr(href)").get()

    if not next_page_url:
        return None

    return next_page_url


# Task 4
def scrape_news(html_content):
    """
    scrape Article Page to return a dictonary with data from that Article.
    """

    selector = Selector(html_content)

    url = selector.css("link[rel*=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    category = selector.css("span.label::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("a.url.fn.n::text").get()
    summary = selector.css(".entry-content p").get()
    reading_time = selector.css("li.meta-reading-time ::text").get()

    news_data = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split()[0]),
        "summary": BeautifulSoup(summary, "html.parser").get_text().strip(),
        "category": category,
    }

    return news_data


# Task 5
def get_tech_news(amount):
    """
        get news from page/ return all of them/ store these news on MongoDB DB.
    """
    get_news_list = []

    url = "https://blog.betrybe.com"

    while len(get_news_list) < amount:
        fetch_main_page = fetch(url)
        news_url_list_on_page = scrape_updates(fetch_main_page)
        for new_url in news_url_list_on_page:
            fetch_article_page = fetch(new_url)
            get_news_list.append(scrape_news(fetch_article_page))
            if (len(get_news_list) == amount):
                break
        url = scrape_next_page_link(fetch_main_page)

    create_news(get_news_list)
    return get_news_list
