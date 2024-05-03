from django.urls import path
from . import views

urlpatterns = [
    path('', views.prompt_list, name='prompt_list'),
    path('prompt/new', views.prompt_create, name='prompt_create'),
    path('prompt/<int:pk>/edit/', views.prompt_update, name='prompt_update'),
    path('prompt/<int:pk>/delete/', views.prompt_delete, name='prompt_delete'),
]
