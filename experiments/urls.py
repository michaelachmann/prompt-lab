from django.urls import path
from . import views

urlpatterns = [
    path('', views.experiment_list, name='experiment_list'),
    path('new', views.experiment_create, name='experiment_create'),
    path('<int:pk>/', views.experiment_detail, name='experiment_detail'),
    path('<int:pk>/edit/', views.experiment_update, name='experiment_update'),
    path('<int:pk>/delete/', views.experiment_delete, name='experiment_delete'),
]
