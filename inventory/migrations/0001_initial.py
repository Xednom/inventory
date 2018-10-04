# Generated by Django 2.1 on 2018-10-01 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_items', models.CharField(max_length=200)),
                ('brand_name', models.CharField(max_length=150)),
                ('size', models.CharField(choices=[('', '------'), ('s', 'Small'), ('m', 'Medium'), ('l', 'Large')], max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]