from .models import Category, SubCategory


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def get_subcategories(request):
    subcategories = SubCategory.objects.all()
    return {'subcategories': subcategories}
