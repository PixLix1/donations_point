from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Profile, Activation
from users.emails import send_activation_email

AuthUserModel = get_user_model()


@receiver(post_save, sender=AuthUserModel)
def create_profile(instance, created, **kwargs):
    # print('*' * 100)
    # print('instance', instance)
    # print('created', created)
    # print('**kwargs', kwargs)

    if created:
        Profile(user=instance).save()
    else:  # do something on update
        pass


@receiver(pre_save, sender=AuthUserModel)
def inactivate_user(instance, **kwargs):
    print('instance', instance)
    if not instance.pk:
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def set_activation_email(instance, created, **kwargs):
    if created:
        print('instance', instance)
        activation = Activation(instance.id)
        activation.save()
        send_activation_email(activation)
