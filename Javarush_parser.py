import json

import requests
from bs4 import BeautifulSoup

#парсер, который собирает последние новости с сайта JavaRush

url = "https://javarush.ru/groups/posts"
r = requests.get(url=url)
soup = BeautifulSoup(r.text, 'html.parser')

#метод, который делает запрос новостей с указанной выше страницы
def get_news():
    post_cards = soup.find_all('a', class_='post-card__link')

    javarush_data_base = {}

 # цикл, который проходит по html и вычленяет параметры названия статьи, ссылку и выбирает для записи уникальный айдишник
    for post in post_cards:
        post_card_title = post.find('h4', class_='post-card__title').text.strip()
        post_url = post.get("href")
        post_id = post_url.split("/")[+5]
        post_id = post_id[:+4]

        javarush_data_base[post_id] = {
            "post_url": post_url,
            "post_title": post_card_title
        }
# складываем выбранные параметры в джейсон-файл
    with open("javarush_data_base.json", "w") as file:
        json.dump(javarush_data_base, file, indent=4, ensure_ascii=False)


def main():
    get_news()


if __name__ == '__main__':
    main()