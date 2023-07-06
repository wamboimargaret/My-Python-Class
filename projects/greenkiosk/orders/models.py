from django.db import models



# Create your models here.
class Orders(models.Model):
   Order_Id = models.IntegerField()
   Order_Date = models.DateTimeField()
   Order_Status = models.CharField(max_length=32)
   Order_Total = models.DecimalField(max_digits=8 ,decimal_places=2)
#    Order_Items = models.JSONField()




