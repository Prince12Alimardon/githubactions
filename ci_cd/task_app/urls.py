from django.urls import path

from .views import *

urlpatterns = [
    path('task/', TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
