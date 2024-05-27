from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_list, name='dataset_list'),
    path('dataset/new', views.dataset_create, name='dataset_create'),
    path('dataset/<int:pk>/edit/', views.dataset_update, name='dataset_update'),
    path('dataset/<int:pk>/delete/', views.dataset_delete, name='dataset_delete'),
]
