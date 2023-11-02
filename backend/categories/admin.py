from django.contrib import admin
from .models import Category, SubCategory, TemporarilyLinksFasrshop, TemporarilyLinksBRRC, TemporarilyLinksAll4rc, \
    TemporarilyLinksHobbyCenter, TemporarilyLinksNitrorcx, TemporarilyLinksRcstore, TemporarilyLinksOptax, \
    TemporarilyLinksShopntoys, TemporarilyLinksUltrarobox, TemporarilyLinksSnt, TemporarilyLinksMicromachine


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_filter = ("category__name",)
    list_display = ("category", "name",)


@admin.register(TemporarilyLinksBRRC)
class TemporarilyLinksBRRCAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksFasrshop)
class TemporarilyLinksFasrshopAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksAll4rc)
class TemporarilyLinksAll4rcAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksHobbyCenter)
class TemporarilyLinksHobbyCenterAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksRcstore)
class TemporarilyLinksRcstoreAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksNitrorcx)
class TemporarilyLinksNitrorcxAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksOptax)
class TemporarilyLinksOptaxAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksShopntoys)
class TemporarilyLinksShopntoysAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksUltrarobox)
class TemporarilyLinksUltraroboxAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksSnt)
class TemporarilyLinksSntAdmin(admin.ModelAdmin):
    pass


@admin.register(TemporarilyLinksMicromachine)
class TemporarilyLinksMicromachineAdmin(admin.ModelAdmin):
    pass
