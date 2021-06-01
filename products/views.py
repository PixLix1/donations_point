from django.shortcuts import render, HttpResponse
from products.models import Category, Products


# Create your views here.
def category_list(request):
    # categories = set(Products.objects.values_list('name', flat=True))  # import single field, return text,
    # not tuple
    print('request:', request.GET.get('name'))
    search_by_name = request.GET.get('name')

    if search_by_name:
        categories = Category.objects.filter(name__icontains=search_by_name)
    else:
        categories = sorted(Category.objects.all(), key=lambda x: x.name)
    return render(request, 'products/category_list.html', {
        'category_list': categories,
    })


def product_list(request, category_id):
    return HttpResponse('I received category id = %s' % category_id)
    # products = Products.objects.all()
    #
    # return render(request, 'products/product_list.html', {
    #     'product_list': products
    # })
