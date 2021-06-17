from django.shortcuts import render, Http404
from django.views.generic import ListView
from products.models import Products
from django.core.paginator import Paginator
from products.forms.filter import SearchItems

# class ItemsList(ListView):
#     model = Products
#     context_object_name = 'items_list'
#     template_name = 'items/list.html'
#     paginate_by = 9


def list_view(request):
    form = SearchItems(request.GET)
    products = form.get_filtered_items()
    # products = products.filter(status__lt=3).exclude(user_id=request.user.id)
    products = products.filter(status__lt=3)
    paginator = Paginator(products, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'items/list.html', {
        'page_obj': page_obj,
        'items_list': products,
        # 'form': form
    })


def item_view(request, item_id):
    try:
        product = Products.objects.get(id=item_id)
    except Products.DoesNotExist:
        raise Http404('Item with ID %s does not exist.' % item_id)

    return render(request, 'items/item.html', {
        'product': product,
    })


def products_by_owner(request, user_id):
    items = Products.objects.filter(user_id=user_id).exclude(status=3)
    product = items[0]
    print('product user first', product.user.first_name)
    first_name = product.user.first_name
    last_name = product.user.last_name
    # print('user slice', user)
    # owner_first_name = user.first_name
    return render(request, 'items/products_by_owner.html', {
        'items': items,
        'first_name': first_name,
        'last_name': last_name,
    })
