from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from main.models import Task

class Command(BaseCommand):
    help = 'Create new User'

    # added number of arguments that support during add_todo command
    # add_argument function described below
    # 1 argument is varibale name
    # 2 argument is type of varibale
    # 3 argument is help text
    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Username')


    def handle(self, *args, **kwargs):
        username = kwargs['username'] # username value passed through command assign it to new username variable
        User.objects.create_user(username)