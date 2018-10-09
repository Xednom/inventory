from rest_framework import serializers
from .models import Item, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name', )


class ItemSerializer(serializers.ModelSerializer):
    category_items = serializers.SlugRelatedField(slug_field='category_name', queryset=Category.objects.all())

    class Meta:
        model = Item
        fields = ('item_id', 'category_items', 'brand_name', 'size', 'price', 'date_added')
