from distutils.command.upload import upload
from msilib.schema import Class
from django.db import models

# Create your models here.




class Signup(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    paswd=models.CharField(max_length=30)
    country=models.CharField(max_length=30)



class Addproduct(models.Model):
    user=models.ForeignKey(Signup,on_delete=models.CASCADE)
    poductname=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.IntegerField()
    img=models.ImageField(upload_to='Product_images/' ,blank=True,null=True)


class ApiUsers(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
   
