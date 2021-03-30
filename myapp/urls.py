from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.test,name='index'),
    path('main', views.test1,name='main'),
    path('home', views.test2,name='home'),
    path('admin-login', views.test3,name='admin-login'),
    path('user-login', views.test4,name='user-login'),
    path('hr-home1', views.test5,name='hr-home1'),
    path('emp-reg1', views.test6,name='emp-reg1'),
    path('reg', views.test7,name='reg'),
    path('add-dept', views.test8,name='add-dept'),
    path('emp-home', views.test9,name='emp-home'),
    path('apply-leave', views.test10,name='apply-leave'),
    path('recruitment-post', views.test11,name='recruitment-post'),
    path('interview', views.test12,name='interview'),
    
]