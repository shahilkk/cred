from django.urls import path
from . import views


urlpatterns = [

    path('dashbord',views.dashbord,name="dashbord"),
    path('login',views.login,name="login"),
    path('home',views.home,name="home"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('createexam',views.createexam,name="createexam"),
    path('questions',views.questions,name="questions"),
    path('master',views.master,name="master"),

]