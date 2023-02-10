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


# Requisito 2
def scrape_updates(html_content):
    """
       scrapes Trybe's main News Page to obtain URL links to specific articles.
    """
    selector = Selector(html_content)
    return selector.css("main[class=site-main] article::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
