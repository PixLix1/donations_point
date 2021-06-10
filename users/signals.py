from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from users.models import Profile, Activation
from users.emails import send_activation_email
from django.conf import settings

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
    if (not instance.pk and
            (not hasattr(instance, 'is_social_auth') or not instance.is_social_auth)):
        instance.is_active = False
        instance.password = None


@receiver(post_save, sender=AuthUserModel)
def set_activation_email(instance, created, **kwargs):
    # login with social acct should not receive activation email (password is saved in db)
    # accounts through register do not have attribute is_social_auth
    # create superuser instance has attribute is_social_auth=False
    # exclude active accounts
    if created and (
            not hasattr(instance, 'is_social_auth') or not instance.is_social_auth) and not instance.is_active:
        activation = Activation(user=instance)
        activation.save()
        send_activation_email(activation)
