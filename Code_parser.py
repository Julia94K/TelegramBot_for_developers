import json

import requests
from bs4 import BeautifulSoup

url = "https://thecode.media/"
r = requests.get(url=url)

soup = BeautifulSoup(r.text, 'html.parser')

def get_news_code():
    post_titles_wide = soup.find_all('a', class_='post post--wide')
    post_titles_medium = soup.find_all('a', class_='post post--medium')
    post_titles_small = soup.find_all('a', class_='post post--small')


    post_all=post_titles_medium+post_titles_wide+post_titles_small

    code_data_base={}

    for post in post_all:
        post_title = post.find('div',class_='post__title').text.strip()
        post_url = post.get("href")
        post_id = post_url.split("/")[3]
        code_data_base[post_id]={
            'post_url':post_url,
            'post_title':post_title
        }
    with open('code_data_base.json','w') as file:
        json.dump(code_data_base,file,indent=4,ensure_ascii=False)



def main():
    get_news_code()


if __name__ == '__main__':
    main()



