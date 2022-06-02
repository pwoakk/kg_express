from rest_framework import serializers

from backend.apps.product.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'slug',
        ]


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'name',
            'slug',
            'category',
        ]


class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer(read_only=True)
    # subcategory = SubCategorySerializer(read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    subcategory = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    # subcategories = SubCategorySerializer(
    #     read_only=True,
    #     many=True, # будет список subcategory
    # )
    subcategories = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'subcategories']



