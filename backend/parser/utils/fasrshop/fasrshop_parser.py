import csv
import urllib.request
from .product_service import create_product


def get_product_info_as_file():
    urllib.request.urlretrieve("https://www.fasrshop.ru/Excel/files/products_all.csv", "fasrshop.csv")


def parse_product_file():
    get_product_info_as_file()
    with open('fasrshop.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # print(row)
            create_product(row)


parse_product_file()
