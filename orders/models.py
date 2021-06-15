from django.db import models
from donations_point.models import CustomModel
from django.contrib.auth import get_user_model
from products.models import Products

AuthUserModel = get_user_model()


# Create your models here.
class Order(CustomModel):
    user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    item = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='order')




# class ProductOrders(CustomModel):
#     user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
#     item = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='products')
#     orders = models.ManyToManyField(Order, through='Products', related_name='order_items')
#
#
# # class Order(CustomModel):
# #     user = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
# #     items = models.ManyToManyField(Products, through='OrderItem', related_name='orders')  # order.items / product.orders
# #
# #
# # class OrderItem(CustomModel):
# #     item = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='order_items')  # product.order_items
# #     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')  # order.order_items
#
#
