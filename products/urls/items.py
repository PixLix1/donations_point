from django.urls import path
from products.views.items import list_view, add_to_favorites, item_view, products_by_owner
from products.views.categories import category_details

app_name = 'items'

urlpatterns = [
    # path('', ItemsList.as_view(), name='list'),
    path('', list_view, name='list'),
    path('<int:item_id>/add_to_favorites/<int:page_num>/>', add_to_favorites, name='add_to_favorites'),
    path('<int:item_id>/add_item_to_favorites/', add_to_favorites, name='add_to_favorites_item_view'),
    path('<int:item_id>/', item_view, name='item'),
    path('category/<int:category_id>/', category_details, name='category'),
    path('<int:user_id>/products_by_owner/', products_by_owner, name='products_by_owner'),
]
