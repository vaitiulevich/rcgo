from datetime import datetime
from categories.models import TemporarilyLinksFasrshop
from categories.utils.services import get_page_soup, str_format, get_num_for_string, convert_price, \
    create_product, save_images, \
    get_fasrshop_supplier, update_product_info
from pytils.translit import slugify


def get_links():
    links_obj = TemporarilyLinksFasrshop.objects.filter(date=datetime.today())
    return links_obj


@str_format(['\r', '\t', '\n'])
def get_name(soup):
    return soup.find('div', class_="alexder-product-title").h1.get_text()


def get_slug(name):
    return slugify(name)


def get_price(soup):
    return float(get_num_for_string(soup.find('span', class_='price').span.get_text())[:-2])


@str_format(['\r', '\t'])
def get_description(soup):
    try:
        return soup.find('div', class_='content-description').get_text()
    except AttributeError:
        return ''


def get_article(soup):
    return soup.find('div', class_='product-block-sku').span.get_text()


def get_brand(soup):
    try:
        return soup.find('div', class_='brands').div.a.get_text()
    except AttributeError:
        return ''


def get_images(soup):
    return [img.img['src'] for img in soup.find_all('a', class_='cm-previewer')]


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
                    'brand': get_brand(soup),
                    'supplier': get_fasrshop_supplier(),
                    'category': category_link.subcategory,
                }
                product_data['slug'] = get_slug(product_data['name'])
                product_data['margin_price'] = convert_price(product_data['price_ru'])
                images = get_images(soup)
                if None not in images:
                    product = create_product(product_data)
                    save_images(images, product)
        category_link.delete()
