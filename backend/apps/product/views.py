from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import SubCategory, Product, BannerImage
from django.views import generic
# Create your views here.


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")


class IndexPage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        banners = BannerImage.objects.all()
        if len(banners) > 6:
            banners = banners[:6]
        context['banners'] = banners
        return context


class ProductListView(generic.ListView):
    template_name = 'product_list.html'
    paginate_by = 6
    model = Product
    # стандартное имя списка продуктов в шаблоне для ListView = object_list

    def get_queryset(self):
        # print(self.kwargs)
        category_slug = self.kwargs.get('slug')
        subcategory_slug = self.kwargs.get('subcategory_slug')
        if subcategory_slug:
            products = Product.objects.filter(is_active=True, subcategory__slug=subcategory_slug)
        elif category_slug:
            products = Product.objects.filter(is_active=True, category__slug=category_slug)
        else:
            products = Product.objects.filter(is_active=True)
        return products


class ProductDetailView(generic.DetailView):
    template_name = 'product_detail.html'
    model = Product
    context_object_name = 'product'     # стандартный это object
    # slug_field = 'id'
    # slug_url_kwarg = 'pk'     # под капотом DetailView сам вытаскивает pk
