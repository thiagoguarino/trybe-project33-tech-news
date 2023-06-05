## Trybe Project 33 - Tech News


## PROJECT OVERVIEW

  This is project #3 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project is a console app that fetches data about news scraped from a [tech blog](https://blog.betrybe.com/). This project has Unit Tests and Bonus Tasks as well. Stack: Python3, Pytest, MongoDB.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

  * tasks 11 and 12 are bonus tasks

  *Description* | *Status*
  --- | :---:
1 - create the function fetch | :heavy_check_mark:
2 - create the function scrape_updates | :heavy_check_mark:
3 - create the function scrape_next_page_link | :heavy_check_mark:
4 - create the function scrape_news | :heavy_check_mark:
5 - create the function get_tech_news para obter as notícias! | :heavy_check_mark:
6 - Test class ReadingPlanService | :heavy_check_mark:
7 - create the function search_by_title | :heavy_check_mark:
8 - create the function search_by_date | :heavy_check_mark:
9 - create the function search_by_category | :heavy_check_mark:
10 - create the function top_5_categories | :heavy_check_mark:
11 - create the function analyzer_menu | :heavy_check_mark:
12 - implement console menu functions | :heavy_check_mark:

</details>

<details>
  <summary><strong>How to Execute the Tests</strong></summary>

  To execute the tests, first check if you have the virtual environment up and running.

  <strong>To Execute All tests:</strong> ```$ python3 -m pytest```

  the file `pyproject.toml` already correctly configures pytest. However, in case you have issues with that and want a complete explicit output, the command is:

  ```bash
  python3 -m pytest -s -vv
  ```

  In case you need to execute just one test file, use the command:

  ```bash
  python3 -m pytest tests/filename.py
  ```

  In case you need to execute just one test function, use the command:

  ```bash
  python3 -m pytest -k test_function_name
  ```

  If you wish that the tests stop from being executed when the first error happens, use the param `-x`

  ```bash
  python3 -m pytest -x tests/filename.py
  ```

  To execute a specific test of a file, type the command:

  ```bash
  python3 -m pytest tests/filename.py::test_function_name
  ```
</details>

  ## HOW TO RUN THE APP


  1. clone the repository

   - `git clone git@github.com:thiagoguarino/trybe-project33-tech-news.git`
  
  2. enter the project's folder 

   - `cd trybe-project33-tech-news`

  3. create and open the project's virtual environment

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  4. install dependencies

  - `python3 -m pip install -r dev-requirements.txt`

  <details>
  <summary><strong>How To Execute the App</strong></summary>

  The news that will be scraped are available at https://blog.betrybe.com. These news must be saved on the apps Database using py functions that were previously built for this project at `database.py` Module.

  This project uses a MongoDB database called "tech_news". The news will be stored in a collection called "news". there are some previously built functions ready on the file `tech_news/database.py` that will help you with the development of the app. Don't alter the functions on this file.

  To run MongoDB via Docker: `docker-compose up -d mongodb` on terminal.

  With the DB running, the apps module will access it correctly. Import the module `tech_news/database.py` and call the functions contained inside. Remember that MongoDB uses port 27017. If there's another service using this port, consider disabling it.

  To execute the app and display the console Menu type: `tech-news-analyzer`
  </details>