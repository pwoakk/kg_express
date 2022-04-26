import json

from django.http import HttpResponse
from django.shortcuts import render

from backend.apps.product.models import SubCategory


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
        category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")
