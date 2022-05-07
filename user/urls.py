from unicodedata import name
from django.urls import path
from . import views





urlpatterns = [
    path('uhome',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('view',views.view,name="view"),
    path('display',views.display,name="display"),
    path('api',views.api,name="api"),
    path('checkexist',views.checkexist,name="checkexist"),
    path('ajax',views.ajax,name="ajax"),
    path('ajaxhtml',views.ajaxhtml,name="ajaxhtml"),
    path('examhome',views.examhome,name="examhome"),
    path('exam/<str:exam_name>,<str:stu_id>',views.exam,name="exam"),
    path('viewanswer',views.viewanswer,name="viewanswer"),

]