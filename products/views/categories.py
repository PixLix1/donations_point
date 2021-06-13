from django.shortcuts import render, Http404, redirect, reverse
from products.models import Category, Products


# Create your views here.
def category_list(request):
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
        # category = Category.objects.get(pk=category_id)
        products = Products.objects.filter(category=category_id)
    except Category.DoesNotExist:
        raise Http404('Category with ID %s does not exist.' % category_id)

    return render(request, 'category_details.html', {
        'product_list': products,
    })

# def product_list(request, category_id):
#     return HttpResponse('I received category id = %s' % category_id)
#     # items = Products.objects.all()
#     #
#     # return render(request, 'items/category_details.html', {
#     #     'product_list': items
#     # })
