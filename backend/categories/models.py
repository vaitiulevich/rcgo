from django.db import models


class Category(models.Model):
    name = models.TextField(verbose_name="Название категории")
    slug = models.TextField(verbose_name="Ссылка на категорию")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    name = models.TextField(verbose_name="Название подкатегории")
    slug = models.TextField(verbose_name="Ссылка на подкатегорию")
    brrc_link = models.TextField(verbose_name="Ссылка на парсинг brrc", null=True, blank=True)
    fasrshop_link = models.TextField(verbose_name="Ссылка на парсинг fasrshop", null=True, blank=True)
    all4rc_link = models.TextField(verbose_name="Ссылка на парсинг all4rc", null=True, blank=True)
    hobbycenter_link = models.TextField(verbose_name="Ссылка на парсинг hobbycenter", null=True, blank=True)
    rcstore_link = models.TextField(verbose_name="Ссылка на парсинг rcstore", null=True, blank=True)
    nitrorcx_link = models.TextField(verbose_name="Ссылка на парсинг nitrorcx", null=True, blank=True)
    optax_link = models.TextField(verbose_name="Ссылка на парсинг optax", null=True, blank=True)
    shopntoys_link = models.TextField(verbose_name="Ссылка на парсинг shopntoys", null=True, blank=True)
    snt_link = models.TextField(verbose_name="Ссылка на парсинг snt", null=True, blank=True)
    micromachine_link = models.TextField(verbose_name="Ссылка на парсинг micromachine", null=True, blank=True)
    ultrarobox_link = models.TextField(verbose_name="Ссылка на парсинг ultrarobox", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories',
                                 verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class TemporarilyLinksBRRC(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка BRRC'
        verbose_name_plural = 'Промежуточная ссылки BRRC'


class TemporarilyLinksFasrshop(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка Fasrshop'
        verbose_name_plural = 'Промежуточная ссылки Fasrshop'


class TemporarilyLinksAll4rc(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка All4rc'
        verbose_name_plural = 'Промежуточная ссылки All4rc'


class TemporarilyLinksHobbyCenter(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка HobbyCenter'
        verbose_name_plural = 'Промежуточные ссылки HobbyCenter'


class TemporarilyLinksRcstore(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка RcStore'
        verbose_name_plural = 'Промежуточные ссылки RcStore'


class TemporarilyLinksNitrorcx(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка Nitrorcx'
        verbose_name_plural = 'Промежуточные ссылки Nitrorcx'


class TemporarilyLinksOptax(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка Optax'
        verbose_name_plural = 'Промежуточные ссылки Optax'


class TemporarilyLinksShopntoys(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка Shopntoys'
        verbose_name_plural = 'Промежуточные ссылки Shopntoys'


class TemporarilyLinksUltrarobox(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка Ulrarobox'
        verbose_name_plural = 'Промежуточные ссылки Ulrarobox'


class TemporarilyLinksSnt(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка Snt'
        verbose_name_plural = 'Промежуточные ссылки Snt'


class TemporarilyLinksMicromachine(models.Model):
    links = models.JSONField(verbose_name="Промежуточные ссылки на парсинг")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Подкатегория')
    date = models.DateField(verbose_name="День временных ссылок", auto_now_add=True)

    def __str__(self):
        return str(self.subcategory.name)

    class Meta:
        verbose_name = 'Ссылка Micromachine'
        verbose_name_plural = 'Промежуточные ссылки Micromachine'
