import requests
import time
from parsel import Selector


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


# Requisito 3
def scrape_next_page_link(html_content):
    """
        scrape Trybe's main News Page to obtain a URL link to next news page
    """
    selector = Selector(html_content)
    next_page_url = selector.css("a.next::attr(href)").get()

    if not next_page_url:
        return None

    return next_page_url


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
