# from asyncio import Task
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'items' #change object_name for task_list.html file

class TaskDescription(DetailView):
    model = Task
    # context_object_name = 'title' 
    template_name = 'main/description.html' #points to 