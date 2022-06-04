from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from backend.apps.product.models import Category, SubCategory, Product
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    SubCategorySerializer,
    CategoryDetailSerializer, ProductCreateSerializer
)


class CategoryListApiView(ListAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class SubCategoryListApiView(ListAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class ProductListApiView(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_active=True)


class CategoryDetailApiView(RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class ProductCreateApiView(CreateAPIView):
    serializer_class = ProductCreateSerializer


