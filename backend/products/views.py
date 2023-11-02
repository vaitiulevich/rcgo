# import django_filters
from rest_framework import generics, filters
from rest_framework.permissions import AllowAny
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from .models import Product
from categories.models import Category, SubCategory
from .serializers import CategorySerializer, ProductSerializer, SubCategorySerializer

exclude_list = ['Колесный транспорт',
                'Игрушки и хобби',
                'Танки',
                'Корабли',
                'Самолеты',
                'Вертолеты',
                'Машины',
                'Квадрокоптеры', ]
filter_list = ['Запчасти по брендам',
               'Запчасти для танков',
               'Запчасти для самолетов',
               'Запчасти для вертолетов',
               'Запчасти для кораблей',
               'Запчасти для машин',
               'Запчасти к квадрокоптерам', ]


class CategoryListView(CacheResponseMixin, generics.ListAPIView):
    queryset = Category.objects.exclude(name__in=exclude_list + filter_list)
    serializer_class = CategorySerializer
    pagination_class = None
    permission_classes = [AllowAny]
    list_cache_timeout = 60 * 10


class SubCategoryListView(CacheResponseMixin, generics.ListAPIView):
    permission_classes = [AllowAny]
    pagination_class = None
    list_cache_timeout = 60 * 5

    def get_queryset(self):
        queryset = SubCategory.objects.all()
        category = self.request.query_params.get('category', None)
        if category is not None:
            if category == 'zapchasti':
                queryset = Category.objects.filter(name__in=filter_list)
            else:
                queryset = queryset.filter(category__slug=category)
        return queryset

    def get_serializer_class(self):
        category = self.request.query_params.get('category', None)
        if category is not None:
            if category == 'zapchasti':
                return CategorySerializer
        return SubCategorySerializer


class ProductListView(CacheResponseMixin, generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    search_fields = ['name', 'article_sup', 'brand', 'category__name', 'category__category__name']
    filter_backends = (filters.SearchFilter,)
    list_cache_timeout = 3600 * 12

    def get_queryset(self):
        queryset = Product.objects.all()

        category = self.request.query_params.get('category', None)
        subcategory = self.request.query_params.get('subcategory', None)
        if category is not None:
            queryset = queryset.filter(category__category__slug=category)
        if subcategory is not None:
            queryset = queryset.filter(category__slug=subcategory)
        return queryset


class ProductDetailView(CacheResponseMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = "slug"
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    object_cache_timeout = 3600 * 24


# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(field_name='name', lookup_expr="icontains")
#     brand = django_filters.CharFilter(field_name='brand', lookup_expr="icontains")
#     article_sup = django_filters.CharFilter(field_name='article_sup', lookup_expr="icontains")
#
#     class Meta:
#         model = Product
#         fields = ['name', 'brand', 'article_sup']


class ProductSearchView(CacheResponseMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    list_cache_timeout = 3600 * 12

    # filterset_class = ProductFilter
