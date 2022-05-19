from django.shortcuts import render, redirect
from django.views import View

from backend.apps.cart.cart import Cart
from backend.apps.cart.forms import CartAddForm
from backend.apps.product.models import Product


class AddCartView(View):

    def post(self, request):
        product_id = self.kwargs.get('pk')
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.add(
            product=product,
        )
        return redirect("index")


class CartDetailView(View):

    def get(self, request):
        return render(self.request, 'cart.html')
