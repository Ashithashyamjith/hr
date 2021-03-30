from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.fnt,name='index'),
    path('hr-home', views.fnt1,name='hr-home'),
]    