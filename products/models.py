from django.db import models
from django.contrib.auth import get_user_model
from donations_point.models import CustomModel

AuthUserModel = get_user_model()

#
# # Create your models here.
# class Products(CustomModel):
#     donor = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE, related_name='stores')
#     name = models.CharField(max_length=255, unique=True)
#     description = models.TextField()
#     logo = models.ImageField(upload_to='stores')
#     delivery_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
#     profit_fee = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
#     ingredients = models.ManyToManyField(Ingredient, through='StoreIngredients', related_name='stores')