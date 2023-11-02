import json
import urllib.request
import pandas as pd
import requests
from bs4 import BeautifulSoup

from parser.utils.optax.product_service import create_product


def get_product_info(excel_data: dict):
    del excel_data['0'], excel_data['1'], excel_data['2']
    for row in excel_data.values():
        if None in [row['1'], row['2'], row['3'], row['5'], row['6'], row['7']]:
            continue
        else:
            pass
            img_desc = get_imgs_and_desc(row['1'])
            desc = "\n".join(line.strip() for line in img_desc[1].splitlines() if line.strip())
            create_product(row['2'], img_desc[0], row['6'], desc, row['5'], row['1'], row['7'], img_desc[2], img_desc[3])


def get_imgs_and_desc(article):
    response = requests.get(f'https://optax.ru/search/?q={article}').text
    soup = BeautifulSoup(response, 'lxml')
    product_link = soup.find('a', class_='picture')['href']
    response = requests.get(f'https://optax.ru{product_link}').text
    product_soup = BeautifulSoup(response, 'lxml')
    categories = product_soup.find('div', {"id": "breadcrumbs"})
    category_list = []
    for cat in categories.find('ul').find_all('li'):
        category_list.append(cat.getText())
    print(category_list)
    if len(category_list) == 7:
        subcategory = 'Другое'
        category = category_list[-3]
    else:
        subcategory = category_list[-3]
        category = category_list[-5]
    if category == 'Распродажа':
        category = 'Аксессуары для фото и видео'
    return product_soup.find_all('a', class_='zoom'), product_soup.find('div', class_='changeDescription').text, category, subcategory


def main():
    urllib.request.urlretrieve("https://optax.ru/upload/optax_price_all_obnov_2907.xlsx", "optax.xlsx")
    excel_data = pd.read_excel('optax.xlsx', names=[1, 2, 3, 4, 5, 6, 7])
    data = pd.DataFrame(excel_data).transpose()
    excel_data = json.loads(data.to_json())
    get_product_info(excel_data)


main()
