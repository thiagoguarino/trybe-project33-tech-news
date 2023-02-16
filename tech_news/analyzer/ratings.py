from tech_news.database import find_news
from collections import Counter


# task 10
def top_5_categories():
    """
    this function will list the top 5 most common news categories on database
    """
    categories_raw_list = list()
    categories_output_list = list()

    get_news = find_news()

    for news in get_news:
        categories_raw_list.append(news["category"])

    cat_counter_dict = Counter(categories_raw_list)

    cat_counter_list_tuples = cat_counter_dict.items()

    cat_sorted_list_tuples = sorted(
        cat_counter_list_tuples,
        key=lambda elem: (-elem[1], elem[0])
    )

    for tuples in cat_sorted_list_tuples[0:5]:
        categories_output_list.append(tuples[0])

    return categories_output_list
