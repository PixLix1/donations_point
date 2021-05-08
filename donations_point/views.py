from django.http import HttpResponse
from django.shortcuts import render


def homepage_view(request):
    return render(request, 'homepage.html', {
        'brand': 'Simple ways',
        'motto': 'Reduce waste at home'
    })


def contact_view(request):
    return render(request, 'contact.html', {})
