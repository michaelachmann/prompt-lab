from django.urls import path
from . import views

urlpatterns = [
    path('', views.prompt_list, name='prompt_list'),
    path('new', views.prompt_create, name='prompt_create'),
    path('<int:pk>/', views.prompt_detail, name='prompt_detail'),
    path('<int:pk>/edit/', views.prompt_update, name='prompt_update'),
    path('<int:pk>/delete/', views.prompt_delete, name='prompt_delete'),
]
