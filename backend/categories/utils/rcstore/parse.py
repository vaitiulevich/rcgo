from categories.models import SubCategory, TemporarilyLinksRcstore
from categories.utils.services import get_page_soup, check_quantity


def get_parse_links():
    subcategories = SubCategory.objects.all()
    for subcategory in subcategories:
        if subcategory.rcstore_link is not None:
            for link in subcategory.rcstore_link.split('\n'):
                if link != '':
                    get_products_link(link, subcategory)


def get_products_link(link, subcategory):
    soup = get_page_soup(link)
    pages_num = soup.find('div', class_='nav-pages')
    if pages_num is None:
        pages_num = 1
    else:
        pages_num = int(max([i for i in pages_num.get_text().split() if i.isdigit()]))
    get_all_pages(link, pages_num, subcategory)


def save_temporarily_links(links, subcategory):
    TemporarilyLinksRcstore.objects.create(links=links, subcategory=subcategory)


def get_all_pages(link, pages_num, subcategory):
    dict_links = {'links': []}
    for i in range(1, pages_num + 1):
        soup = get_page_soup(f"{link}?page={i}")
        links = soup.find_all('div', class_='product-card')
        for product_link in links:
            link_result = f"https://rcstore.ru{product_link.find('div', class_='product-card__img').a['href']}"
            if product_link.find('a', class_="btn btn-orange btn-small not-availible") is None:
                dict_links['links'].append(link_result)
            else:
                check_quantity(link_result)
    if dict_links['links']:
        save_temporarily_links(dict_links, subcategory)
