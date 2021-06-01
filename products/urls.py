from django.urls import path
from products.views import category_list, product_list

app_name = 'products'

urlpatterns = [
    path('', category_list, name='list'),
    path('<int:category_id>/', product_list, name='products')
]