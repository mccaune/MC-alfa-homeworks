from django.urls import path, include
from app import views


urlpatterns = [
    path('', views.list, name='list'),
    path('list_region/<r_id>', views.list_region, name='list-region'),
    path('list_continent/<c_id>', views.list_continent, name='list-continent'),
    path('countries/edit/<int:pk>/', views.edit, name='edit'),
]