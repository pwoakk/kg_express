from django.urls import path
from .views import IndexPage, get_subcategory

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('getSubCategory/', get_subcategory, name='get_subcategory')
]