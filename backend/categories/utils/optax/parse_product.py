import re
from datetime import datetime
from categories.models import TemporarilyLinksOptax
from categories.utils.services import get_page_soup, str_format, get_num_for_string, convert_price, \
    create_product, save_images, \
    get_optax_supplier, update_product_info
from pytils.translit import slugify


def get_links():
    links_obj = TemporarilyLinksOptax.objects.filter(date=datetime.today())
    return links_obj


@str_format(['\r', '\t', '\n'])
def get_name(soup):
    return soup.find('h1', class_="changeName").get_text()


def get_slug(name):
    return slugify(name)


def get_price(soup):
    try:
        return float(get_num_for_string(soup.find('span', class_='priceVal').get_text()))
    except AttributeError:
        print(soup)


@str_format(['\r', '\t', '\xa0'])
def get_description(soup):
    try:
        return soup.find('div', class_='changeDescription').get_text().replace('\n\n', '').replace('Подробнее',
                                                                                                   '')
    except AttributeError:
        return ''


def get_article(soup):
    return soup.find('span', class_='changeArticle').get_text()


def get_images(soup):
    return ['https://optax.ru/'+img.a['href'] for img in soup.find('div', class_='slideBox').find_all('div', class_='item')]


def main():
    links = get_links()
    for category_link in links:
        for link in category_link.links['links']:
            soup = get_page_soup(link)
            price = get_price(soup)
            if update_product_info(link, price):
                product_data = {
                    'name': get_name(soup),
                    'price_ru': price,
                    'supp_link': link,
                    'description': get_description(soup),
                    'article_sup': get_article(soup),
                    'quantity_composition': 'В наличии',
                    'category': category_link.subcategory,
                    'supplier': get_optax_supplier(),
                }
                product_data['slug'] = get_slug(product_data['name'])
                product_data['margin_price'] = convert_price(product_data['price_ru'])
                images = get_images(soup)
                product = create_product(product_data)
                save_images(images, product)
        category_link.delete()
