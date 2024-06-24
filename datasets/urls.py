from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataset_list, name='dataset_list'),
    path('new/', views.dataset_create, name='dataset_create'),
    path('<int:pk>/', views.dataset_detail, name='dataset_detail'),
    path('<int:pk>/edit/', views.dataset_update, name='dataset_update'),
    path('<int:pk>/delete/', views.dataset_delete, name='dataset_delete'),
    path('tag-list/', views.tag_list, name='tag-list'),
    path('dataset/<int:pk>/edit/', views.DatasetEditView.as_view(), name='dataset_edit'),
]
