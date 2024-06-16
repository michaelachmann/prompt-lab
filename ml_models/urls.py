from django.urls import path
from . import views

urlpatterns = [
    path('', views.ml_model_list, name='ml_model_list'),
    path('ml_model/new', views.ml_model_create, name='ml_model_create'),
    path('<int:pk>/', views.ml_model_detail, name='ml_model_detail'),
    path('ml_model/<int:pk>/edit/', views.ml_model_update, name='ml_model_update'),
    path('ml_model/<int:pk>/delete/', views.ml_model_delete, name='ml_model_delete'),
]


