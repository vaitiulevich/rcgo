from rest_framework import serializers
from .models import Product, ProductImage
from categories.models import Category, SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        try:
            return f"https://rcgo.by/{str(ProductImage.objects.filter(product__category__name=obj.name, product__category__category__name=obj.category.name)[0].img_low)}"
        except IndexError:
            return None

    class Meta:
        model = SubCategory
        fields = ['name', 'slug', 'image']


class CategorySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        try:
            img = f"https://rcgo.by/{str(ProductImage.objects.filter(product__category__category__name=obj.name)[0].img_low)}"
        except IndexError:
            return None
        return img

    class Meta:
        model = Category
        fields = ['name', 'slug', 'image']


class ImageSerializer(serializers.ModelSerializer):
    img_low = serializers.SerializerMethodField()
    img_medium = serializers.SerializerMethodField()
    img_high = serializers.SerializerMethodField()

    def get_img_low(self, obj):
        return f"https://rcgo.by/{obj.img_low}"

    def get_img_medium(self, obj):
        return f"https://rcgo.by/{obj.img_medium}"

    def get_img_high(self, obj):
        return f"https://rcgo.by/{obj.img_high}"

    class Meta:
        model = ProductImage
        fields = ['img_low', 'img_medium', 'img_high']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.category.name')
    category_slug = serializers.StringRelatedField(source='category.category.slug')
    subCategory = serializers.StringRelatedField(source='category.name')
    subCategory_slug = serializers.StringRelatedField(source='category.slug')
    images = ImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['name',
                  'id',
                  'slug',
                  'category_slug',
                  'subCategory_slug',
                  'price_ru',
                  'margin_price',
                  'price_usd',
                  'dealer_price_ru',
                  'description',
                  'article_sup',
                  'quantity_composition',
                  'quantity',
                  'brand',
                  'characteristics',
                  'category',
                  'subCategory',
                  'images']
