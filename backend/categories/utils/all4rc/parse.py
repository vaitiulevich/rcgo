from categories.models import SubCategory, TemporarilyLinksAll4rc
from categories.utils.services import get_page_soup, check_quantity


def get_parse_links():
    subcategories = SubCategory.objects.all()
    for subcategory in subcategories:
        if subcategory.all4rc_link is not None:
            for link in subcategory.all4rc_link.split('\n'):
                if link != '':
                    get_products_link(link, subcategory)


def get_products_link(link, subcategory):
    soup = get_page_soup(link)
    pages_num = soup.find('div', class_='bx-pagination-container')
    if pages_num is None:
        pages_num = 1
    else:
        pages_num = int(max([i for i in pages_num.get_text().split('\n') if i.isdigit()]))
    get_all_pages(link, pages_num, subcategory)


def save_temporarily_links(links, subcategory):
    TemporarilyLinksAll4rc.objects.create(links=links, subcategory=subcategory)


def get_all_pages(link, pages_num, subcategory):
    dict_links = {'links': []}
    for i in range(1, pages_num + 1):
        soup = get_page_soup(f"{link}?PAGEN_1={i}")
        links = soup.find_all('div', class_='tabloid')
        for product_link in links:
            link_result = f"https://www.all4rc.ru{product_link.find('div', class_='productColImage').a['href']}"
            if product_link.find('a', class_="outOfStock") is None:
                dict_links['links'].append(link_result)
            else:
                check_quantity(link_result)
    if dict_links['links']:
        save_temporarily_links(dict_links, subcategory)


