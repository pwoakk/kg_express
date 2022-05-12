from django.urls import path
from .views import IndexPage, get_subcategory, ProductListView, ProductDetailView

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('getSubCategory/', get_subcategory, name='get_subcategory'),
    path('list/product/', ProductListView.as_view(), name='product_list'),
    path('list/product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('list/category/<slug:slug>/', ProductListView.as_view(), name='category_products'),
    path('list/category/<slug:slug>/<slug:subcategory_slug>/', ProductListView.as_view(), name='subcategory_products'),

]