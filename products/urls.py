from django.urls import path
from products.views import product_list

app_name = 'products'

urlpatterns = [
    path('', product_list, name='list')
]