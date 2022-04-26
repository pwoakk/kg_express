from django.contrib import admin
from django.urls import path, include

from backend.apps.product.views import get_subcategory

urlpatterns = [
    path('getSubcategory/', get_subcategory, name='get_subcategory'),
]