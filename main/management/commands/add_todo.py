from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from main.models import Task

class Command(BaseCommand):
    help = 'Create new Todo'

    # added number of arguments that support during add_todo command
    # add_argument function described below
    # 1 argument is varibale name
    # 2 argument is type of varibale
    # 3 argument is help text
    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')
        parser.add_argument('title', type=str, help='Todo title')
        parser.add_argument('description', type=str, help='Todo description')
        parser.add_argument('complete', type=bool, help='Todo completed')

    def handle(self, *args, **kwargs):
        username = kwargs['username'] # username value passed through command assign it to new username variable
        user = User.objects.get(username = username) # using ORM getting user object becuase we have to pass user object during creation of new Task
        title = kwargs['title'] # title value passed through command assign it to new title variable
        description = kwargs['description'] # description value passed through command assign it to new description variable
        complete = kwargs['complete'] # complete value passed through command assign it to new complete variable
        Task.objects.create(user = user, title = title, description = description, complete = complete) # creating new Task