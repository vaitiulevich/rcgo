from datetime import datetime
from categories.models import TemporarilyLinksAll4rc
from categories.utils.services import get_page_soup, str_format, get_num_for_string, convert_price, create_product, save_images, \
    get_all4rc_supplier, update_product_info
from pytils.translit import slugify


def get_links():
    links_obj = TemporarilyLinksAll4rc.objects.filter(date=datetime.today())
    return links_obj


@str_format(['\r', '\t', '\n'])
def get_name(soup):
    return soup.find('h1', class_="changeName").get_text()


def get_slug(name):
    return slugify(name)


def get_price(soup):
    return float(get_num_for_string(soup.find('span', class_='priceVal').get_text()))


@str_format(['\r', '\t'])
def get_description(soup):
    try:
        return soup.find('div', class_='changeDescription').get_text()
    except AttributeError:
        return ''


def get_article(soup):
    return soup.find('span', class_='changeArticle').get_text()


def get_images(soup):
    images = ['https://www.all4rc.ru/' + img.a['href'] for img in soup.find('div', class_='slideBox').find_all('div', class_='item')]
    if not images:
        images = ['https://www.all4rc.ru/' + img.a['href'] for img in soup.find('div', class_='pictureSlider').find_all('div', class_='item')]
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
                    'supplier': get_all4rc_supplier(),
                }
                product_data['slug'] = get_slug(product_data['name'])
                product_data['margin_price'] = convert_price(product_data['price_ru'])
                images = get_images(soup)
                product = create_product(product_data)
                save_images(images, product)
        category_link.delete()
