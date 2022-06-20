from asyncio import Task
from django.urls import path
from .views import TaskList,TaskDescription

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDescription.as_view(), name='task'),
]