from django.urls import path
from products.views.favorites import favorites_view, add_to_favorites, remove_from_favorites

app_name = 'favorites'

urlpatterns = [
    path('', favorites_view, name='view'),
    # path('', remove_from_favorites, name='remove'),
    path('<int:item_id>/add_to_favorites/<int:page_num>/>', add_to_favorites, name='add_to_favorites'),
    path('<int:item_id>/add_item_to_favorites/', add_to_favorites, name='add_to_favorites_item_view'),
    path('<int:item_id>/remove_favorite/', remove_from_favorites, name='remove_favorite'),
]
