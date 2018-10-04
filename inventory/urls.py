from django.urls import path
from . import views

app_name = 'inventorys'
urlpatterns = [
    path('', views.index, name='index'),
    path('tshirt/', views.TshirtListView.as_view(), name='tshirt'),
    path('acccesories/', views.AccesoriesListView.as_view(), name='acce'),
    path('shoes/', views.ShoesListView.as_view(), name='shoes'),
    path('inventory/', views.InventoryAddView.as_view(), name='inventory_add'),
]
