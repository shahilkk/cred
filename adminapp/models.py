from django.db import models

# Create your models here.





class Registration(models.Model): 
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Exam(models.Model):
    title =models.CharField(max_length=30)


class Question(models.Model):
    title_name =models.CharField(max_length=30)
    question =models.CharField(max_length=30)
    option1 =models.CharField(max_length=30)
    option2 =models.CharField(max_length=30)
    option3 =models.CharField(max_length=30)
    option4 =models.CharField(max_length=30)
    mark =models.CharField(max_length=30)
    answer =models.CharField(max_length=30)
    

       