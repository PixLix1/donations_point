from django.shortcuts import redirect, reverse, render, Http404
from django.views.generic import ListView
from products.models import Products
from utils.favorites import Favorites


class ItemsList(ListView):
    model = Products
    context_object_name = 'items_list'
    template_name = 'items/list.html'
    paginate_by = 9


def add_to_favorites(request, item_id):
    page = request.GET.get('page', 1)
    next_url = request.GET.get('next')
    favorites = Favorites(request.user, request.session)
    favorites.add(item_id)

    if next_url:
        return redirect(next_url)

    return redirect('%s?page=%s' % (
        reverse('products:items:list'),
        page
    ))


def item_view(request, item_id, page=None):
    try:
        product = Products.objects.get(id=item_id)
    except Products.DoesNotExist:
        raise Http404('Item with ID %s does not exist.' % item_id)

    return render(request, 'items/item.html', {
        'product': product,
        'page': page
    })
