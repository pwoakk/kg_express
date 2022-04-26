from django.contrib import admin

from backend.apps.product.models import Product, Category, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'id']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('id', 'name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'slug',
        'id',
    )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'image',
        'category',
        'subcategory',
        'created',
        'updated',
        'is_active',
    ]