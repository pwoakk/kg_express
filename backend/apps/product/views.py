from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
import json

from django_filters.views import FilterView

from .filters import ProductFilter
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


class ProductListView(FilterView):
    template_name = 'product_list.html'
    paginate_by = 6
    model = Product
    # стандартное имя списка продуктов в шаблоне для ListView = object_list
    filterset_class = ProductFilter

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


class ProductSearchView(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    paginate_by = 6

    def get_queryset(self):
        search_text = self.request.GET.get('query')
        if search_text is None:
            return self.model.objects.filter(is_active=True)
        queryset = self.model.objects.filter(
            Q(name__icontains=search_text)
            | Q(description__icontains=search_text)
            | Q(category__name__icontains=search_text)
        )
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductSearchView, self).get_context_data(**kwargs)
        context['search'] = True
        context['search_query'] = self.request.GET.get('query')
        return context

