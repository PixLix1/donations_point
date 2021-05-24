from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Profile

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    print('*' * 100)
    print('instance', instance)
    print('created', created)
    print('**kwargs', kwargs)

    if created:
        Profile(user=instance).save()
    else:  # do something on update
        pass
