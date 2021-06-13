from django.urls import path
from products.views.items import ItemsList, add_to_favorites, item_view
from products.views.categories import category_details

app_name = 'items'

urlpatterns = [
    path('', ItemsList.as_view(), name='list'),
    path('<int:item_id>/add_to_favorites/>', add_to_favorites, name='add_to_favorites'),
    path('<int:item_id>/', item_view, name='item'),
    path('category/<int:category_id>/', category_details, name='category'),
]
