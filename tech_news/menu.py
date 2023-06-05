import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.analyzer.ratings import top_5_categories


# file authorship: thiago guarino
def news_by_quantity():
    user_input = input("Digite quantas notícias serão buscadas: ")
    return get_tech_news(int(user_input))


def news_by_title():
    user_input = input("Digite o título: ")
    return search_by_title(user_input)


def news_by_date():
    user_input = input("Digite a data no formato aaaa-mm-dd: ")
    return search_by_date(user_input)


def news_by_category():
    user_input = input("Digite a categoria: ")
    return search_by_category(user_input)


def top_categories():
    return top_5_categories()


def exit_app():
    return "Encerrando script"


function = {
    "0": news_by_quantity,
    "1": news_by_title,
    "2": news_by_date,
    "3": news_by_category,
    "4": top_categories,
    "5": exit_app,
}

menu_text = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por categoria;
 4 - Listar top 5 categorias;
 5 - Sair.
 """


def analyzer_menu():
    try:
        chosen_option = input(menu_text+"OPÇÃO: ")
        return print(function[chosen_option]())
    except Exception:
        sys.stderr.write("Opção inválida\n")
