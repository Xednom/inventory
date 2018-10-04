from django.db import models


class Item(models.Model):
    SMALL = 's'
    MEDIUM = 'm'
    LARGE = 'l'
    SIZES = (
        ('', '------'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )
    item_id = models.AutoField(primary_key=True)
    category_items = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=150)
    size = models.CharField(max_length=100, choices=SIZES)
    price = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_items
