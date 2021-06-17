from django.urls import path
from orders.views import request_product, requests_orders, owner_view_orders, process_order, user_view_requests

app_name = 'orders'

urlpatterns = [
    path('', requests_orders, name='requests_orders'),
    path('your_requests/', user_view_requests, name='donation_requests'),
    path('your_orders/', owner_view_orders, name='view_orders'),
    path('<int:item_id>/request/', request_product, name='request_donation'),
    path('<int:order_id>/order/', process_order, name='process_order'),
]
