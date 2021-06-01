from django.db import models
from django.contrib.auth import get_user_model
from donations_point.models import CustomModel

AuthUserModel = get_user_model()


# Create your models here.
class Category(CustomModel):
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='categories')


class Products(CustomModel):
    user = models.ForeignKey(AuthUserModel, null=False, on_delete=models.CASCADE, related_name='users')
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=255)
    image_url = models.TextField()
