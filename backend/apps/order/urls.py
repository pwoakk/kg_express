from django.urls import path

from backend.apps.order.views import OrderCreateView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='order_create'),
]