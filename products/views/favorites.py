from django.shortcuts import render, redirect, reverse
from products.models import Products
from utils.favorites import Favorites
from django.urls import resolve


def favorites_view(request):
    favorites = request.session.get('favorites', {})
    favorites_list = Products.objects.filter(id__in=favorites.keys())

    # if request.POST:
    #     for key, value in request.POST.items():
    #         if key.startswith('remove_'):
    #             item_id = key[7:]
    #             favorites = Favorites(request.user, request.session)
    #             favorites.remove(item_id)
    #             return redirect(reverse('products:favorites:view'))

    return render(request, 'favorites/view.html', {
        'items_list': favorites_list,
    })


def add_to_favorites(request, item_id, page_num=None):
    # next_url = request.GET.get('next')
    favorites = Favorites(request.user, request.session)
    favorites.add(item_id)

    current_url = resolve(request.path_info).url_name
    previous_url = request.META['HTTP_REFERER']

    if current_url == 'add_to_favorites_item_view':
        return redirect(reverse('products:items:item', args=(item_id,)))

    if 'search_term' in previous_url:
        return redirect(previous_url)

    return redirect('%s?page=%s' % (
        reverse('products:items:list'),
        page_num
    ))


def remove_from_favorites(request, item_id):
    favorites = Favorites(request.user, request.session)
    favorites.remove(item_id)
    return redirect(reverse('products:favorites:view'))
