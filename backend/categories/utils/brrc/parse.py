from categories.models import SubCategory, TemporarilyLinksBRRC

from categories.utils.services import get_page_soup, check_quantity


def get_parse_links():
    subcategories = SubCategory.objects.all()
    for subcategory in subcategories:
        if subcategory.brrc_link is not None:
            for link in subcategory.brrc_link.split('\n'):
                if link != '':
                    get_products_link(link, subcategory)


def get_products_link(link, subcategory):
    soup = get_page_soup(link)
    pages_num = soup.find('div', class_='modern-page-navigation')
    if pages_num is None:
        pages_num = 1
    else:
        pages_num = int(max([i for i in pages_num.get_text().split('\n') if i.isdigit()]))
    get_all_pages(link, pages_num, subcategory)


def save_temporarily_links(links, subcategory):
    TemporarilyLinksBRRC.objects.create(links=links, subcategory=subcategory)


def get_all_pages(link, pages_num, subcategory):
    dict_links = {'links': []}
    for i in range(1, pages_num + 1):
        soup = get_page_soup(f"{link}?PAGEN_2={i}")
        links = soup.find_all('div', class_='product-item')
        for product_link in links:
            link_result = f"https://brrc.ru{product_link.a['href']}"
            if product_link.find('span', class_="catalog-item-avaliability") is None:
                dict_links['links'].append(link_result)
            else:
                check_quantity(link_result)
    if dict_links['links']:
        save_temporarily_links(dict_links, subcategory)
