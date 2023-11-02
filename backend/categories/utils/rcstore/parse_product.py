import re
from datetime import datetime
from categories.models import TemporarilyLinksRcstore
from categories.utils.services import get_page_soup, str_format, get_num_for_string, convert_price, create_product,\
     save_images, get_rcstore_supplier, update_product_info
from pytils.translit import slugify


def get_links():
    links_obj = TemporarilyLinksRcstore.objects.filter(date=datetime.today())
    return links_obj


@str_format(['\r', '\t', '\n'])
def get_name(soup):
    return soup.find('h1', class_="product-page__title").get_text()


def get_slug(name):
    return slugify(name)


def get_price(soup):
    try:
        return float(get_num_for_string(soup.find('span', class_='product-page__price').get_text()))
    except AttributeError:
        print(soup)


@str_format(['\r', '\t', '\xa0'])
def get_description(soup):
    try:
        return soup.find('div', class_='description-des').get_text().replace('\n\n', '').replace('Подробнее', '')
    except AttributeError:
        return ''


def get_article(soup):
    return re.search(r'Артикул: (.+)', soup.find('span', class_='product-page__article').get_text()).group(1)


def get_images(soup):
    images = ['https://rcstore.ru/'+img['href'] for img in soup.find_all('a', class_='product-page__preview-img')]
    images.append('https://rcstore.ru/'+soup.find('div', class_='product-page__lg-image-slider').a['href'])
    return images


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
                    'supplier': get_rcstore_supplier(),
                }
                product_data['slug'] = get_slug(product_data['name'])
                product_data['margin_price'] = convert_price(product_data['price_ru'])
                images = get_images(soup)
                product = create_product(product_data)
                save_images(images, product)
        category_link.delete()
