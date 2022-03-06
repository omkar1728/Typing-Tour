from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/',views.home,name='home'),
    path('/dashboard',views.dashboard,name=  'dashboard'),
    path('/keyboard',views.keyboard,name='keyboard'),
    path('/levels',views.levels,name='levels'),
    path('/practice',views.pracitce,name='practice'),
    path('/profile',views.profile,name='profile'),
    

]

