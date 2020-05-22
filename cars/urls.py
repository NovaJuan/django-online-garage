from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cars'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_car, name='add_car'),
    path('delete/<int:car_id>/', views.remove_car, name='remove_car'),
    path('update/<int:car_id>/', views.update_car, name='update_car'),
    path('details/<int:car_id>/', views.details, name='details'),
    path('details/<int:car_id>/review', views.review, name='reviews'),
    path('details/<int:car_id>/review/<int:review_id>/delete',
         views.remove_review, name='remove_review'),
]
