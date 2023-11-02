from datetime import datetime
from categories.models import TemporarilyLinksBRRC
from categories.utils.services import get_page_soup, str_format, get_num_for_string, convert_price, create_product, save_images, \
    get_brrc_supplier, update_product_info
from pytils.translit import slugify
import re


# возможно придется добавить характеристики

def get_links():
    links_obj = TemporarilyLinksBRRC.objects.filter(date=datetime.today())
    return links_obj


@str_format(['\r', '\t', '\n'])
def get_name(soup):
    return soup.find('div', class_="element-wrapper").h1.get_text()


def get_slug(name):
    return slugify(name)


def get_price(soup):
    return float(get_num_for_string(soup.find('div', class_='product-item-detail-price-current').get_text()))


@str_format(['\r', '\t'])
def get_description(soup):
    try:
        return soup.find('div', class_='product-item-detail-tab-content').get_text()
    except AttributeError:
        return ''


def get_article(soup):
    return re.search(r'Артикул: (.+)', soup.find('div', class_='element-artnumber').get_text()).group(1)


def get_images(soup):
    return ['https://brrc.ru/' + img.img['src'] for img in soup.find_all('div', class_='product-item-detail-slider-image')]


def main():
    links = get_links()
    for category_link in links:
        for link in category_link.links['links']:
            soup = get_page_soup(link)
            try:
                price = get_price(soup)
            except AttributeError:
                print(link, category_link.subcategory, flush=True)
                continue
            if update_product_info(link, price):
                product_data = {
                    'name': get_name(soup),
                    'price_ru': price,
                    'supp_link': link,
                    'description': get_description(soup),
                    'article_sup': get_article(soup),
                    'quantity_composition': 'В наличии',
                    'category': category_link.subcategory,
                    'supplier': get_brrc_supplier(),
                }
                product_data['slug'] = get_slug(product_data['name'])
                product_data['margin_price'] = convert_price(product_data['price_ru'])
                images = get_images(soup)
                product = create_product(product_data)
                save_images(images, product)
        category_link.delete()
