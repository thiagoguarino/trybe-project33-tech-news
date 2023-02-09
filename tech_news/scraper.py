import requests
import time


# Task 1
def fetch(url):

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
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
