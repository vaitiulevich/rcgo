import PIL
from django.db import IntegrityError
from pytils.translit import slugify
from products.models import Category, ProductImage, Product, SubCategory, Rates
import tempfile
from urllib.request import urlopen, Request
from django.core.files import File


def get_category(category1):
    try:
        category = category1[0].lower()
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
        res = category1[0]
    return res


def create_product(name, photo, price, brend, description, quantity, article, characteristics, category):
    if quantity == 0:
        return None
    article_sup = article
    quantity_composition = quantity
    name = name
    if len(category) > 1:
        subcategory = category[1]
    else:
        subcategory = brend
    category = get_category(category)
    if category is None:
        return None
    elif category == 'ДВС':
        category = 'Двигатели'
        subcategory = 'ДВС'
    brend = brend
    price_ru = price['retail']
    dealer_price_ru = price['dealer']
    photo = photo
    description = description
    if Product.objects.filter(article_sup=article_sup):
        product = Product.objects.get(article_sup=article_sup)
        if quantity_composition == '0':
            return None
        product.price_ru = float(price_ru)
        product.dealer_price_ru = float(dealer_price_ru)
        product.margin_price = round(float(price_ru) / 100 * Rates.objects.latest("id").rus, 2)
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
        subcategory = SubCategory(name=subcategory,category=category, slug=slugify(subcategory))
        subcategory.save()
    product = Product(
        name=name,
        price_ru=float(price_ru),
        slug=slugify(name),
        margin_price=round(float(price_ru) / 100 * Rates.objects.latest("id").rus,2),
        dealer_price_ru=float(dealer_price_ru),
        description=description,
        article_sup=article_sup,
        quantity_composition=quantity_composition,
        brand=brend,
        category=subcategory,
        characteristics=characteristics
    )
    for img in photo:
        img_temp = tempfile.NamedTemporaryFile(delete=True)
        req = Request(str(img.img['src']))
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')
        img_temp.write(urlopen(req).read())
        img_pr = ProductImage(image_url=img.img['src'], product=product)
        try:
            img_pr.img.save('img.jpg', File(img_temp))
        except PIL.UnidentifiedImageError:
            pass
        img_pr.save()
        img_temp.flush()
