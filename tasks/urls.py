from django.urls import path, include
from . import views
from .api import urls as api_urls

urlpatterns = [
    # Regular views (non-API)
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),

    # Include API urls
    path('api/', include(api_urls)),
]
