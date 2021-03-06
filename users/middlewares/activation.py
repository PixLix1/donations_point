from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils import timezone
from users.models import Activation


class ValidateTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        token = view_kwargs.get('token')

        activation = get_object_or_404(Activation, token=token, activated_at=None)
        reset_token_route = reverse('users:activation:reset_token', args=(token,))
        activate_route = reverse('users:activation:activate', args=(token,))
        is_reset_token_route = request.path == reset_token_route
        # print('request.path', request.path)
        if activation.expires_at < timezone.now():
            if is_reset_token_route:
                return None
            else:
                return redirect(reset_token_route)

        if is_reset_token_route:
            return redirect(activate_route)
