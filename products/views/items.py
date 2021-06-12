from django.shortcuts import redirect, reverse
from django.views.generic import ListView
from products.models import Products


class ItemsList(ListView):
    model = Products
    context_object_name = 'items_list'
    template_name = 'items/list.html'
    paginate_by = 9


def add_to_favorites(request, item_id):
    product = Products.objects.get(pk=item_id)
    page = request.POST.get('page', 1)

    if 'favorites' in request.session:
        request.session['favorites'].update({item_id: product.name})
        request.session.modified = True
    else:
        request.session['favorites'] = {
            item_id: product.name
        }

    print('req_session', request.session['favorites'])

    return redirect('%s?page=%s' % (
        reverse('products:items:list'),
        page
    ))
