from django.urls import path
from . import views

urlpatterns = [
  path('about/', views.about, name='about'),
  path('dogs/', views.dogs_index, name='index'),
  path('dogs/<int:dog_id>', views.dogs_detail, name='detail'),
]