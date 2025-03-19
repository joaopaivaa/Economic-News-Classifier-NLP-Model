import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Função para obter o HTML de uma página
def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'lxml')


def cnn_scraper():

    # CNN Brasil

    df = pd.DataFrame(columns=['date','journal','title','text'])

    main_page = get_html("https://www.cnnbrasil.com.br/economia/")

    sections = main_page.select("div.col__l--4")

    for i in range(1):
        section = sections[i]
        news = section.select('ul.block__news__list')[0].select('li.block__news__item')

        for page in news:
            link = page.select('a')[0]['href']
            title = page.select('figure')[0].select('h3.block__news__title')[0].text.strip()

            news_page = get_html(link)

            text_array = news_page.select('div.single-content')[0].select('p')

            full_text = ''
            for text_block in text_array:
                full_text = full_text + text_block.text + ' '
            full_text = full_text.strip()

            df_page = pd.DataFrame([{
                'date':date.today().strftime("%d-%m-%Y"),
                'journal':'CNN Brasil',
                'title':title,
                'text':full_text
            }])

            df = pd.concat([df, df_page], ignore_index=True)

    return df


def infomoney_scraper():

    # InfoMoney

    df = pd.DataFrame(columns=['date','journal','title','text'])

    main_page = get_html("https://www.infomoney.com.br/economia/")

    pages = main_page.select("div.w-full[data-ds-component='card-sm']")

    for page in pages:

        link = page.select('a')[1]['href']
        title = page.select('a')[1].text.strip()

        news_page = get_html(link)

        text_array = news_page.select('article')[0].select('p:not([class])')

        full_text = ''
        for text_block in text_array:
            full_text = full_text + text_block.text + ' '
        full_text = full_text.strip()

        df_page = pd.DataFrame([{
            'date':date.today().strftime("%d-%m-%Y"),
            'journal':'InfoMoney Brasil',
            'title':title,
            'text':full_text
        }])

        df = pd.concat([df, df_page], ignore_index=True)

    return df


def get_news():
    cnn_news = cnn_scraper()
    infomoney_news = infomoney_scraper()

    news = pd.concat([cnn_news, infomoney_news], ignore_index=True)

    return news

past_news = pd.read_csv(BASE_DIR + "/Brazilian News Database.csv", sep=';', encoding="utf-8")

today_news = get_news()

news = pd.concat([past_news, today_news], ignore_index=True)
news.to_csv(BASE_DIR + "/Brazilian News Database.csv", sep=';', encoding="utf-8", index=False)
