from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

# reference: 
# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html#introduction
# https://docs.python.org/3/library/argparse.html
class Command(BaseCommand):
    help = 'Delete user by Username'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='username')

    def handle(self, *args, **kwargs):
        username = kwargs['username']

        try:
            user = User.objects.get(username=username)
            user_id = user.id
            user.delete()
            self.stdout.write(self.style.SUCCESS('User "%s (%d)" deleted with success!' % (user.username, user_id)))
        except User.DoesNotExist:
            self.stdout.write(self.style.WARNING('User with username "%s" does not exist.' % username))


        # for user_id in users_ids:
        #     try:
        #         user = User.objects.get(pk=user_id)
        #         user.delete()
        #         self.stdout.write(self.style.SUCCESS('User "%s (%s)" deleted with success!' % (user.username, user_id)))
        #     except User.DoesNotExist:
        #         self.stdout.write(self.style.WARNING('User with id "%s" does not exist.' % user_id))