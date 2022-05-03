from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import SubCategory, Product
from django.views import generic
# Create your views here.


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class IndexPage(generic.TemplateView):
    template_name = "index.html"


class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    paginate_by = 20
    model = Product
    queryset = Product.objects.filter(is_active=True)
    context_object_name = 'products'
    # стандартное имя списка продуктов в шаблоне для ListView = object_list


class ProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'     # стандартный это object
    # slug_field = 'id'
    # slug_url_kwarg = 'pk'     # под капотом DetailView сам вытаскивает pk
