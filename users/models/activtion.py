import secrets
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from donations_point.models import CustomModel
from utils.constants import ACTIVATION_AVAILABILITY_DICT

AuthUserAuth = get_user_model()


class Activation(CustomModel):
    user = models.OneToOneField(AuthUserAuth, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, default=secrets.token_hex(32))
    expires_at = models.DateTimeField(default=timezone.now() + timezone.timedelta(**ACTIVATION_AVAILABILITY_DICT))
    activated_at = models.DateTimeField(null=True, default=None)

