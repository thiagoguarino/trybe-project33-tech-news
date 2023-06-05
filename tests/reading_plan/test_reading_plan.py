from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from tech_news.analyzer import reading_plan
from unittest.mock import patch
import pytest

# file authorship: thiago guarino


@pytest.fixture
def find_news_mock():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-python",
            "title": "Python é a linguagem mais quente do momento",
            "timestamp": "01/01/1940",
            "writer": "John Lennon",
            "reading_time": 6,
            "summary": "Python é top",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-c#",
            "title": "C# é a linguagem mais quente do momento",
            "timestamp": "01/01/1941",
            "writer": "Paul McCartney",
            "reading_time": 8,
            "summary": "C# é top",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-java",
            "title": "Java é a linguagem mais quente do momento",
            "timestamp": "01/01/1942",
            "writer": "George Harrison",
            "reading_time": 15,
            "summary": "Java é top",
            "category": "Ferramentas",
        },
    ]


@pytest.fixture
def group_news_for_available_time_mock():
    return {
        "readable": [
            {"chosen_news": [
                ("Python é a linguagem mais quente do momento", 6)
            ], "unfilled_time": 4},
            {"chosen_news": [
                ("C# é a linguagem mais quente do momento", 8)
            ], "unfilled_time": 2},
        ],
        "unreadable": [
            ("Java é a linguagem mais quente do momento", 15)
            ],
    }


def test_reading_plan_group_news(
    find_news_mock,
    group_news_for_available_time_mock
        ):
    value_error_msg = "Valor 'available_time' deve ser maior que zero"
    with pytest.raises(ValueError, match=value_error_msg):
        ReadingPlanService.group_news_for_available_time(-10)

    with patch.object(
        reading_plan,
        "find_news",
        return_value=find_news_mock
    ):
        real_output = ReadingPlanService.group_news_for_available_time(10)
        expected_output = group_news_for_available_time_mock
        assert real_output == expected_output
