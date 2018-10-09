from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=200, null=True, blank=True, unique=True)

    def __unicode__(self):
        return self.category_name

    def __str__(self):
        return self.category_name


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
    category_items = models.ForeignKey('Category', related_name='category', on_delete=models.DO_NOTHING, null=True, blank=True)
    brand_name = models.CharField(max_length=150)
    size = models.CharField(max_length=100, choices=SIZES)
    price = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.category_items

    def __str__(self):
        return str(self.category_items)
