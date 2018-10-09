from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    View,
    ListView,
    TemplateView
    )

from rest_framework import viewsets, filters
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer


class TshirtListView(ListView):
    model = Item
    template_name = 'inventory/tshirt.html'
    context_object_name = 'all_tshirt'

    def get_queryset(self):
        queryset = Item.objects.filter(category_items__category_name='Tshirt')
        return queryset


class AccesoriesListView(ListView):
    model = Item
    template_name = 'inventory/accesories.html'
    context_object_name = 'all_acce'

    def get_queryset(self):
        queryset = Item.objects.filter(category_items__category_name='Accesories')
        return queryset


class ShoesListView(ListView):
    model = Item
    template_name = 'inventory/shoes.html'
    context_object_name = 'all_shoes'

    def get_queryset(self):
        queryset = Item.objects.filter(category_items__category_name='Shoes')
        return queryset


class InventoryAddView(ListView):
    model = Item
    template_name = 'inventory/inventory.html'

    def get(self, request):
        return render (request, self.template_name)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = (filters.SearchFilter,)
    serach_fields = ('brand_name')


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def index(request):
    return render(request, 'inventory/index.html')
