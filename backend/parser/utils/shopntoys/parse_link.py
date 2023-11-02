import requests
from bs4 import BeautifulSoup


def get_products_link():
    open('products_link.txt', 'w')
    with open('links.txt', 'r') as file:
        products = []
        for i in file:
            response = requests.get(i).text
            soup = BeautifulSoup(response, 'html.parser')
            max_paginate = soup.find_all('a', class_="c-pagination-item")
            max_paginate = [int(pag.get_text()) for pag in max_paginate if pag.get_text().isdigit()]
            if max_paginate:
                for page in range(1, max(max_paginate) + 1):
                    response = requests.get(i.replace('\n', '') + '?page=' + str(page)).text
                    soup = BeautifulSoup(response, 'html.parser')
                    products_links = soup.find_all('a', class_='l-image-box_fill')
                    for link in products_links:
                        products.append('https://shopntoys.ru/' + link['href'] + '\n')
            else:
                response = requests.get(i).text
                soup = BeautifulSoup(response, 'html.parser')
                products_links = soup.find_all('a', class_='l-image-box_fill')
                for link in products_links:
                    products.append('https://shopntoys.ru/' + link['href'] + '\n')
    with open('products_link.txt', 'w') as file:
        file.writelines(products)


get_products_link()
