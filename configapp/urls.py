
from django.contrib import admin
from django.urls import path,include
from configapp.views import *
urlpatterns = [

    path('',index, name="home"),
    path('add_room',add_room, name="add_room"),
    path('room_list',room_list, name="room_list"),
    path('user_list',room_list, name="user_list"),


]





