from django.urls import path
from products.views.favorites import favorites_view, remove_from_favorites

app_name = 'favorites'

urlpatterns = [
    path('', favorites_view, name='view'),
    path('', remove_from_favorites, {}, name='remove'),

]
