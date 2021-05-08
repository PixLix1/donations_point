from django.urls import path, include
from django.contrib.auth import views as auth_views

# localhost:8000/users
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html')),
    path('', include('django.contrib.auth.urls')),
]
