from django.db import models

# Create your models here.
class Stock(models.Model): 
    medicine_name = models.CharField(max_length=30)
    medicine_per = models.CharField(max_length=30)
    medicine_qunatity = models.IntegerField()
    medicine_sellingprice = models.CharField(max_length=30)