from django.urls import path
from orders.views import request_product, get_orders, owner_view_orders

app_name = 'orders'

urlpatterns = [
    path('', get_orders, name='requests'),
    path('your_orders/', owner_view_orders, name='view_orders'),
    path('<int:item_id>/your_requests/', request_product, name='request_donation')
]
