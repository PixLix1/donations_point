from django.db import models
from django.contrib.auth import get_user_model
from donations_point.models import CustomModel
from utils.constants import ACTIVE_STATUS, INACTIVE_STATUS, REQUESTED_STATUS
from django.db.models import Count

AuthUserModel = get_user_model()


# Create your models here.
class Category(CustomModel):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Products(CustomModel):
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    user = models.ForeignKey(AuthUserModel, null=False, on_delete=models.CASCADE, related_name='users')
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=255)
    image_url = models.TextField()

    class Status(models.IntegerChoices):
        ACTIVE = ACTIVE_STATUS
        INACTIVE = INACTIVE_STATUS
        REQUESTED = REQUESTED_STATUS

    status = models.IntegerField(choices=Status.choices, null=False, default=ACTIVE_STATUS)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Favorites(CustomModel):
    user = models.OneToOneField(AuthUserModel, on_delete=models.CASCADE)
    data = models.JSONField(null=True)

