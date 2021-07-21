from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Profile

AuthModel = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = AuthModel.objects.filter(profile=None).all()
        for user in users:
            # print(user)
            # if not user.profile:
            Profile(user=user).save()
        print('Added profile to %s users' % len(users))
