from categories.models import SubCategory, TemporarilyLinksHobbyCenter
from categories.utils.services import get_page_soup, check_quantity


def get_parse_links():
    subcategories = SubCategory.objects.all()
    for subcategory in subcategories:
        if subcategory.hobbycenter_link is not None:
            for link in subcategory.hobbycenter_link.split('\n'):
                if link != '':
                    get_products_link(link, subcategory)


def get_products_link(link, subcategory):
    soup = get_page_soup(link)
    pages_num = soup.find('ul', class_='pagination')
    if pages_num is None:
        pages_num = 1
    else:
        pages_num = int(max([i for i in pages_num.get_text().split('\n') if i.isdigit()]))
    print(pages_num)
    get_all_pages(link, pages_num, subcategory)


def save_temporarily_links(links, subcategory):
    TemporarilyLinksHobbyCenter.objects.create(links=links, subcategory=subcategory)


def get_all_pages(link, pages_num, subcategory):
    dict_links = {'links': []}
    for i in range(1, pages_num + 1):
        soup = get_page_soup(f"{link}?page={i}")
        links = soup.find_all('div', class_='card4')
        for product_link in links:
            link_result = f"https://hobbycenter.ru{product_link.a['href']}"
            try:
                if product_link.find_all('div', class_="card4__status-text")[1]:
                    check_quantity(link_result)
            except IndexError:
                dict_links['links'].append(link_result)
    if dict_links['links']:
        save_temporarily_links(dict_links, subcategory)
