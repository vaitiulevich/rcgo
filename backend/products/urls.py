from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailView, ProductSearchView, SubCategoryListView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('subcategories/', SubCategoryListView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<str:slug>/', ProductDetailView.as_view()),
    path('products-search/', ProductSearchView.as_view()),
]
