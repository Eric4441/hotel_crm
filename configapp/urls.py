from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('rooms/', views.room_list, name='room_list'),   # o'zgartirdik
    path('users/', views.users_list, name='users_list'),
    path('deals/', views.deal_list, name='deal_list'),   # o'zgartirdik
    path('search/', views.global_search, name='global_search'),
]
