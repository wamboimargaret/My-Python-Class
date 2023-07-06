from django.contrib import admin

# Register your models here.
from.models import Product_Cart

class Product_cartAdmin(admin.ModelAdmin):
    list_display=("product_name", "product_price", "product_quantity", "product_image", "date_added")

admin.site.register(Product_Cart, Product_cartAdmin)