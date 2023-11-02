from django.contrib import admin
from .models import ProductImage, Product, Supplier, Rates


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Rates)
class RatesAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "category__name", "article_sup")
    list_filter = ("supplier__name", )
    list_display = ("category", "name", "article_sup")
