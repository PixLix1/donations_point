from django.urls import path
from products.views.items import ItemsList, add_to_favorites

app_name = 'items'

urlpatterns = [
    path('', ItemsList.as_view(), name='list'),
    path('<int:item_id>/add_to_favorites/>', add_to_favorites, name='add_to_favorites'),
]
