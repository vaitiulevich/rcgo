import PIL
import requests
from bs4 import BeautifulSoup
from django.core.files.base import ContentFile
from products.models import Product, Rates, Supplier, ProductImage

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


def get_page_soup(link):
    response = requests.get(link, headers=headers).text
    return BeautifulSoup(response, 'lxml')


def str_format(exclude_symbols):
    def decorator(func):
        def wrapper(*args):
            str1 = func(*args)
            for symbol in exclude_symbols:
                str1 = str1.replace(symbol, '').strip()
            return str1

        return wrapper

    return decorator


def get_num_for_string(str1):
    return ''.join([i for i in str1 if i.isdigit()])


def convert_price(price):
    margin_price = price / 100 * Rates.objects.latest("id").rus
    if margin_price < 5:
        margin_price *= 2.5
    elif margin_price < 20:
        margin_price *= 2
    elif margin_price < 100:
        margin_price *= 1.6
    elif margin_price < 500:
        margin_price *= 1.4
    elif margin_price < 1000:
        margin_price *= 1.35
    else:
        margin_price *= 1.3
    return round(margin_price)


def get_brrc_supplier():
    return Supplier.objects.get(name="brrc.ru")


def get_fasrshop_supplier():
    return Supplier.objects.get(name="fasrshop.ru")


def get_all4rc_supplier():
    return Supplier.objects.get(name="all4rc.ru")


def get_hobbycenter_supplier():
    return Supplier.objects.get(name="hobbycenter.ru")


def get_rcstore_supplier():
    return Supplier.objects.get(name="rcstore.ru")


def get_nitrorcx_supplier():
    return Supplier.objects.get(name="nitrorcx.ru")


def get_optax_supplier():
    return Supplier.objects.get(name="optax.ru")


def get_shopntoys_supplier():
    return Supplier.objects.get(name="shopntoys.ru")


def get_ultrarobox_supplier():
    return Supplier.objects.get(name="ultrarobox.ru")


def get_micromachine_supplier():
    return Supplier.objects.get(name="micromachine.ru")


def get_snt_supplier():
    return Supplier.objects.get(name="snt.ru")


def create_product(product_data):
    return Product.objects.create(**product_data)


def save_images(images, product):
    for img in images:
        r = requests.get(img, headers=headers)
        obj = ProductImage(image_url=img, product=product)
        content_file = ContentFile(r.content)
        try:
            obj.img_low.save('img.jpg', content_file)
        except PIL.UnidentifiedImageError:
            product.delete()
            return None
        obj.img_medium.save('img.jpg', content_file)
        obj.img_high.save('img.jpg', content_file)
        obj.save()


def update_product_info(link, price):
    products = Product.objects.filter(supp_link=link)
    if products:
        product = products[0]
        product.price_ru = float(price)
        product.margin_price = convert_price(price)
        product.save()
        return False
    else:
        return True


def check_quantity(link):
    products = Product.objects.filter(supp_link=link)
    if products:
        products[0].delete()
