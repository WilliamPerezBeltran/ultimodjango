
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'shorturl'
urlpatterns = [
    path('', views.index,name="index"),
    path('convert_url/', views.convert_url,name="convert_url"),
]
