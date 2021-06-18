from django.http import HttpResponse
from django.shortcuts import render
from products.models import Products


def homepage_view(request):
    active_items = Products.objects.filter(status__lt=3).count()
    return render(request, 'homepage.html', {
        'brand': 'Simple ways',
        'motto': 'Reduce waste at home',
        'active_items': active_items
    })


def contact_view(request):

    return render(request, 'contact.html', {})
