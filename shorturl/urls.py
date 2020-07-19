
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'shorturl'
urlpatterns = [
    path('', views.index,name="index"),
    path('<str:short_url>', views.get_url,name="get_url"),
]
