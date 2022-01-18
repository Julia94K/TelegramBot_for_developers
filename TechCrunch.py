import json

import requests
from bs4 import BeautifulSoup


url = "https://techcrunch.com/"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, 'html.parser')

def get_news():
    article_cards = soup.find_all('a', class_='article-card__link')

    techcrunch_data_base = {}


    for article in article_cards:
        article_card_title = article.find('h4', class_='article-card__title').text.strip()
        article_url = article.get("href")
        article_id = article_url.split("/")[+5]
        article_id = article_id[:+4]

        techcrunch_data_base[article_id] = {
            "article_url": article_url,
            "article_title": article_card_title
        }

    with open("javarush_data_base.json", "w") as file:
        json.dump(techcrunch_data_base, file, indent=4, ensure_ascii=False)


def main():
    get_news()


if __name__ == '__main__':
    main()
