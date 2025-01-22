import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
from datetime import datetime, timedelta
import time

# Configuração do diretório de trabalho
os.chdir(r"C:\Users\joaov\Documents\NLP Model")

# Função para obter o HTML de uma página
def get_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'lxml')

def scraper():

    # DataFrame para armazenar os imóveis exibidos
    displayed_properties = pd.DataFrame()

    ### Pedro Granado Imóveis

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
            print(full_text)








scraper()