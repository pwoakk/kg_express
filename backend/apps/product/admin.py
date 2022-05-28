from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from .models import *
from django import forms


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'id'
    ]
    prepopulated_fields = {"slug": ('name',)}


@admin.register(SubCategory)
class SubCategory(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'id')
    prepopulated_fields = {"slug": ('name',)}
    list_filter = ("category",)
    search_fields = ("id", "name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = [
        'name',
        'image',
        'category',
        'subcategory',
        'created',
        'updated',
        'is_active'
    ]


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_link', 'image', 'created']
    list_filter = ('created',)
