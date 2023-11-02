import csv
import requests
from bs4 import BeautifulSoup

from parser.utils.brrc.product_service import create_product

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


def get_csv():
    with open("brrc.csv", 'wb') as f:
        f.write(
            requests.get('https://brrc.ru/opt_pricelists/price_opt/price_opt.csv?v=#RAND_STRING#',
                         headers=headers).content)


def parse_csv():
    get_csv()
    with open('brrc.csv', 'r', encoding='windows-1251') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            response = requests.get(row['Ссылка на сайте'], headers=headers).text
            soup = BeautifulSoup(response, 'lxml')
            imgs = soup.find_all('div', class_='product-item-detail-slider-image')
            categories = soup.find_all('div', class_='bx-breadcrumb-item')
            category_list = []
            for i in categories:
                category_list.append(i.get_text().replace('\n', ''))
            description = soup.find('div', class_='product-item-detail-tab-content').get_text()
            create_product(row['Название товара'], imgs, row['Розничная цена'], row['Бренд'], description,
                           row['Остаток на складе'], row['Артикул'], category_list, row['Оптовая цена'],
                           row['Ссылка на сайте'])


parse_csv()
