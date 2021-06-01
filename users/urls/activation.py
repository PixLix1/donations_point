from django.urls import path
from users.views.activation import activate_view

app_name = 'activation'

urlpatterns = [
    path('activate/', activate_view, name='activate')
]