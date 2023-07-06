from django.contrib import admin

# Register your models here.
from .models import Orders

class Orders_admin(admin.ModelAdmin):
    list_display= ("Order_Id","Order_Date","Order_Status","Order_Total")

admin.site.register(Orders,Orders_admin)       
