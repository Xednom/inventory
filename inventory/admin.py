from django.contrib import admin
from . models import Item, Category

# Register your models here.


class ItemProfile(admin.ModelAdmin):
    list_display = ('category_items', 'brand_name', 'size', 'price', 'date_added')


admin.site.register(Item, ItemProfile)
admin.site.register(Category)
