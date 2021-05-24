from django.urls import path
from products.views.list import products_list

app_name = 'products_list'

urlpatterns = [
    path('', products_list, name='list')
]