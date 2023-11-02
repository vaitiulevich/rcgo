import PIL
from bs4 import BeautifulSoup
from django.db import IntegrityError
from pytils.translit import slugify
import tempfile
from urllib.request import urlopen, Request
from django.core.files import File

from products.models import Category, ProductImage, Product, SubCategory, Rates


def get_category(category):
    category_arr = category.split('///')
    category = category.lower()
    if 'машин' in category:
        res = 'Машины'
    elif 'квадрокоптер' in category:
        res = 'Квадрокоптеры'
    elif 'вертолет' in category:
        res = 'Вертолеты'
    elif 'самолет' in category:
        res = 'Самолеты'
    elif 'катер' in category or 'яхт' in category:
        res = 'Катера и яхты'
    elif 'танк' in category:
        res = 'Танки'
    elif 'игруш' in category or 'хобби' in category:
        res = 'Игрушки и хобби'
    elif 'запчас' in category and 'модел' in category:
        res = 'Запчасти для моделей'
    elif 'колесн' in category and 'транспорт' in category:
        res = 'Колесный транспорт'
    else:
        try:
            res = category_arr[1]
        except IndexError:
            return None
    try:
        res2 = category_arr[2]
    except IndexError:
        res2 = 'Другое'
    return res, res2


def get_description(text):
    soup = BeautifulSoup(text, 'lxml')
    return soup.get_text()


def create_product(data):
    article_sup = data['Артикул']
    quantity_composition = data['Склад']
    name = data['Наименование']
    categories = get_category(data['Категория'])
    if categories is None:
        return None
    category = categories[0]
    subcategory = categories[1]
    brend = data['Изготовитель']
    price_ru = data['Розничная цена']
    dealer_price_ru = data['Дилерская цена']
    photo = data['Фотография']
    description = get_description(data['Описание'])
    if Product.objects.filter(article_sup=article_sup):
        product = Product.objects.get(article_sup=article_sup)
        if quantity_composition == '0':
            product.delete()
            return None
        product.price_ru = float(price_ru.replace(',', '.'))
        product.dealer_price_ru = float(dealer_price_ru.replace(',', '.'))
        product.margin_price = round(float(price_ru.replace(',', '.')) / 100 * Rates.objects.latest("id").rus, 2)
        product.quantity_composition = quantity_composition
        product.save()
        return None
    if quantity_composition == '0':
        return None

    if category in Category.objects.values_list('name', flat=True):
        category = Category.objects.get(name=category)
    else:
        category = Category(name=category, slug=slugify(category))
        category.save()
    if subcategory in SubCategory.objects.values_list('name', flat=True):
        subcategory = SubCategory.objects.get(name=subcategory)
    else:
        subcategory = SubCategory(name=subcategory, category=category,slug=slugify(subcategory))
        subcategory.save()
    product = Product(
        name=name,
        slug=slugify(name),
        price_ru=float(price_ru.replace(',', '.')),
        margin_price=round(float(price_ru.replace(',', '.')) / 100 * Rates.objects.latest("id").rus, 2),
        dealer_price_ru=float(dealer_price_ru.replace(',', '.')),
        description=description,
        article_sup=article_sup,
        quantity_composition=quantity_composition,
        brand=brend,
        category=subcategory,
    )
    product.save()
    img_temp = tempfile.NamedTemporaryFile(delete=True)
    req = Request(str(photo))
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
    img_temp.write(urlopen(req).read())
    img_pr = ProductImage(image_url=photo, product=product)
    try:
        img_pr.img.save('img.jpg', File(img_temp))
    except PIL.UnidentifiedImageError:
        pass
    img_pr.save()
    img_temp.flush()

