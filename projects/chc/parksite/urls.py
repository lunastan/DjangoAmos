from django.urls import path, include
from . import views

app_name = 'parksite'

urlpatterns = [
    path('', views.index),
    path('charts.html/', views.charts),
    path('index/', views.index),
]

