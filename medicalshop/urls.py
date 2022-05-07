from django.urls import path
from . import views


urlpatterns = [

    path('master',views.master,name="master"),
    path('home',views.home,name="home"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('bill',views.bill,name="bill"),
    path('Purchase',views.Purchase,name="Purchase"),
    path('billgenerate',views.billgenerate,name="billgenerate"),
    path('add',views.add,name="add"),
    path('search_list',views.search_list,name="search_list"),
    path('search',views.search,name="search"),
    path('update',views.update,name="update"),
]