from django.shortcuts import render, Http404
from products.models import Category, Products


# Create your views here.
def category_list(request):
    # categories = set(Products.objects.values_list('name', flat=True))  # import single field, return text,
    # not tuple
    # print('request:', request.GET.get('name'))
    search_by_name = request.GET.get('name')

    if search_by_name:
        categories = Category.objects.filter(name__icontains=search_by_name)
    else:
        categories = sorted(Category.objects.all(), key=lambda x: x.name)
    return render(request, 'list.html', {
        'category_list': categories,
    })


# list of items linked to category id
def category_details(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404('Category with ID %s does not exist.' % category_id)

    return render(request, 'details.html', {
        'category': category
    })

# def product_list(request, category_id):
#     return HttpResponse('I received category id = %s' % category_id)
#     # items = Products.objects.all()
#     #
#     # return render(request, 'items/details.html', {
#     #     'product_list': items
#     # })
