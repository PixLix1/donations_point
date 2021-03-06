from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views.account import register_view, profile_view

app_name = 'account'

urlpatterns = [
    path('logout', auth_views.auth_logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', register_view, name='register'),
    path('social-auth/', include('social_django.urls')),
    path('profile/', profile_view, name='profile')
]
