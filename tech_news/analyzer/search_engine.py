from tech_news.database import db
from datetime import datetime


# task 7
def search_by_title(title):
    """
        this function will search news on database by title
    """
    news_list = list()

    get_news = db.news.find({"title": {"$regex": title, "$options": 'i'}})

    for news in get_news:
        news_tuple = (news["title"], news["url"])
        news_list.append(news_tuple)

    return news_list


# task 8
def search_by_date(date_input):
    """
        this function will search news on database by date
    """
    news_list = list()

    try:
        original_date_format = datetime.strptime(date_input, '%Y-%m-%d')
        new_date_format = original_date_format.strftime('%d/%m/%Y')

        get_news = db.news.find({"timestamp": {"$regex": new_date_format}})

        for news in get_news:
            news_tuple = (news["title"], news["url"])
            news_list.append(news_tuple)

        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# task 9
def search_by_category(category):
    """
        this function will search news on database by category
    """
    news_list = list()

    get_news = db.news.find({"category": {
        "$regex": category, "$options": 'i'}})

    for news in get_news:
        news_tuple = (news["title"], news["url"])
        news_list.append(news_tuple)

    return news_list
