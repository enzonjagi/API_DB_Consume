from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.get_meals, name="get_meals"),
    path('meals/<int:id>/', views.meal_detail, name="meal_detail")
]