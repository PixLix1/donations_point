from django.shortcuts import render
from products.models import Products


# Create your views here.
def product_list(request):

    products = Products.objects.all()

    return render(request, 'list.html', {
        'product_list': products,
    })
    # return request
