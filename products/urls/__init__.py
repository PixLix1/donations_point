from django.urls import path, include
from products.views.categories import category_list, category_details

app_name = 'products'

urlpatterns = [
    path('', category_list, name='list'),
    path('<int:category_id>/', category_details, name='details'),
    path('items/', include('products.urls.items')),
    # path('', item_view, name='item')
]
