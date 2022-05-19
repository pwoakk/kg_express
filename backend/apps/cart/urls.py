from django.urls import path

from backend.apps.cart.views import AddCartView, CartDetailView

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>/', AddCartView.as_view(), name='add_cart'),
]
