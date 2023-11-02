from categories.models import SubCategory, TemporarilyLinksFasrshop

from categories.utils.services import get_page_soup, check_quantity


def get_parse_links():
    subcategories = SubCategory.objects.all()
    for subcategory in subcategories:
        if subcategory.fasrshop_link is not None:
            for link in subcategory.fasrshop_link.split('\n'):
                if link != '':
                    get_products_link(link, subcategory)


def get_products_link(link, subcategory):
    soup = get_page_soup(link)
    pages_num = soup.find('ul', class_='pagination')
    if pages_num is None:
        pages_num = 1
    else:
        pages_num = int(max([i for i in pages_num.get_text().split('\n') if i.isdigit()]))
    get_all_pages(link, pages_num, subcategory)


def save_temporarily_links(links, subcategory):
    TemporarilyLinksFasrshop.objects.create(links=links, subcategory=subcategory)


def get_all_pages(link, pages_num, subcategory):
    dict_links = {'links': []}
    for i in range(1, pages_num + 1):
        soup = get_page_soup(f"{link}page-{i}/")
        links = soup.find_all('div', class_='thumbnail')
        for product_link in links:
            link_result = product_link.find('div', class_='grid-list-image').a['href']
            if product_link.find('span', class_="btn-stock") is None:
                dict_links['links'].append(link_result)
            else:
                check_quantity(link_result)
    if dict_links['links']:
        save_temporarily_links(dict_links, subcategory)
