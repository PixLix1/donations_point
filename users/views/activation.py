from django.shortcuts import HttpResponse


def activate_view(request, token):
    return HttpResponse('token = %s' % token)
