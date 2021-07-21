from django.urls import path, include
from products.views.categories import category_list, category_details
from products.views.items import item_view

app_name = 'products'

urlpatterns = [
    path('items/', include('products.urls.items')),
    path('favorites/', include('products.urls.favorites')),
]
