from django.urls import path

from backend.apps.api.views import (
    CategoryListApiView,
    SubCategoryListApiView,
    ProductListApiView,
    CategoryDetailApiView, ProductCreateApiView)

urlpatterns = [
    path('category_list/', CategoryListApiView.as_view()),
    path('subcategory_list/', SubCategoryListApiView.as_view()),
    path('product_list/', ProductListApiView.as_view()),
    path('category/detail/<int:pk>/', CategoryDetailApiView.as_view()),
    path('create/product/', ProductCreateApiView.as_view()),
]