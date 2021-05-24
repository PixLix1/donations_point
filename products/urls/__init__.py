from django.urls import path, include
from products.views.list import products_list

app_name = 'products'

urlpatterns = [
    path('', products_list, name='list'),
]
