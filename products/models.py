from django.db import models
from django.contrib.auth import get_user_model
from donations_point.models import CustomModel

AuthUserModel = get_user_model()


# Create your models here.
class Products(CustomModel):
    user_id = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='users')
    category = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    image_url = models.TextField()
