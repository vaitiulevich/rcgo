import PIL
from django.db import IntegrityError
from pytils.translit import slugify
from products.models import Category, ProductImage, Product, SubCategory, Rates
import tempfile
from urllib.request import urlopen, Request
from django.core.files import File


def get_category(category):
    try:
        category = category.lower()
    except IndexError:
        return None
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
        res = category
    return res


def create_product(name, photo, price, description, quantity, article, currancy, category, subcategory):
    article_sup = article
    quantity_composition = quantity
    name = name
    subcategory = subcategory
    category = get_category(category)
    photo = photo
    description = description
    if Product.objects.filter(article_sup=article_sup):
        if currancy == 'USD':
            product = Product.objects.get(article_sup=article_sup)
            if quantity_composition == '0':
                return None
            product.price_usd = float(price)
            product.margin_price = round(float(price) * Rates.objects.latest("id").usd, 2)
            product.quantity_composition = quantity_composition
            product.save()
            return None
        elif currancy == 'RUB':
            product = Product.objects.get(article_sup=article_sup)
            if quantity_composition == '0':
                return None
            product.price_ru = float(price)
            product.margin_price = round(float(price) / 100 * Rates.objects.latest("id").rus, 2)
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
        subcategory = SubCategory(name=subcategory, category=category, slug=slugify(subcategory))
        subcategory.save()
    if currancy == 'USD':
        product = Product(
            name=name,
            slug=slugify(name),
            description=description,
            margin_price=round(float(price) * Rates.objects.latest("id").usd, 2),
            price_usd=price,
            article_sup=article_sup,
            quantity_composition=quantity_composition,
            category=subcategory,
        )
    elif currancy == 'RUB':
        product = Product(
            name=name,
            slug=slugify(name),
            description=description,
            price_ru=price,
            margin_price=round(float(price) / 100 * Rates.objects.latest("id").rus, 2),
            article_sup=article_sup,
            quantity_composition=quantity_composition,
            category=subcategory,
        )
    product.save()
    for img in photo:
        img_temp = tempfile.NamedTemporaryFile(delete=True)
        req = Request(str('https://optax.ru' + img['href']))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        img_temp.write(urlopen(req).read())
        img_pr = ProductImage(image_url='https://optax.ru' + img['href'], product=product)
        try:
            img_pr.img.save('img.jpg', File(img_temp))
        except PIL.UnidentifiedImageError:
            pass
        img_pr.save()
        img_temp.flush()
