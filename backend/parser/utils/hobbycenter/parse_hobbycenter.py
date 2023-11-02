import requests

from parser.utils.hobbycenter.product_service import create_product

token = '6FOyghUexk'


def get_brand_ids():
    brand_ids = requests.get(f'http://api.opthc.ru/v1/getBrands?key={token}').json()
    brand_ids = [brand["id"] for brand in brand_ids]
    return brand_ids


def get_product_extend_description(description):
    from bs4 import BeautifulSoup
    try:
        table = BeautifulSoup(description, 'html.parser')
    except TypeError:
        return {}
    data = "\n".join(line.strip() for line in table.get_text().splitlines() if line.strip())
    return data


def main():
    for brand_id in get_brand_ids():
        products = requests.get(f'http://api.opthc.ru/v1/getProducts?s[brand_id]={brand_id}&key={token}').json()
        for product in products:
            if product is not None or product != '':
                if product['extended_description'] != '':
                    create_product(product['name_rus'], product['photo'], product['price'], product['brand']['name'],
                                   get_product_extend_description(product['extended_description']), product['qty_free'],
                                   product['article'], {i['name']: i['value'] for i in product['specifications']},
                                   [i['name'] for i in product['category_list']])


main()
