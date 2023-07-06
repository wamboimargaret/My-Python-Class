# Generated by Django 4.2.2 on 2023-06-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=32)),
                ('product_price', models.IntegerField()),
                ('product_quantity', models.IntegerField()),
                ('product_image', models.ImageField(upload_to='')),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]