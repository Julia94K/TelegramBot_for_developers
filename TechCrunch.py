import json

import requests
from bs4 import BeautifulSoup


url = "https://techcrunch.com/"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, 'html.parser')

def get_news_tech1():
    article_cards = soup.find_all('a', class_='post-block__title__link')

    techcrunch_data_base = {}

    for article in article_cards:
        title = article.text
        url = (article['href'])
        id = url.split("/")[+6]
        print(title)
        print(url)
        print(id)

        techcrunch_data_base[id] = {
            "article_url": url,
            "article_title": title
            }


    # for article in article_cards:
    #     article_card_title = article.find('h4', class_='article-card__title').text.strip()
    #     article_url = article.get("href")
    #     article_id = article_url.split("/")[+5]
    #     article_id = article_id[:+4]
    #     print("hey")
    #     print(article_id)
    #     print(article_url)
    #     print(article_card_title)
    #
    #
    #     techcrunch_data_base[article_id] = {
    #         "article_url": article_url,
    #         "article_title": article_card_title
    #     }

    with open("techcrunch_data_base.json", "w") as file:
        json.dump(techcrunch_data_base, file, indent=4, ensure_ascii=False)


def main():
    get_news_tech1()


if __name__ == '__main__':
    main()
