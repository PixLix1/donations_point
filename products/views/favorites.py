from django.shortcuts import render, redirect, reverse
from products.models import Products
from utils.favorites import Favorites


def favorites_view(request):
    favorites = request.session.get('favorites', {})
    favorites_list = Products.objects.filter(id__in=favorites.keys())

    if request.POST:
        for key, value in request.POST.items():
            if key.startswith('remove_'):
                item_id = key[7:]
                favorites = Favorites(request.user, request.session)
                favorites.remove(item_id)
                # # print(f'Key: {key}')
                # # print(f'Value: {value}')
                # item_id = key[7:]
                # # print('item_id', item_id, type(item_id))
                # del request.session['favorites'][item_id]
                # request.session.modified = True
                # # print('favorites', request.session['favorites'])
                return redirect(reverse('products:favorites:view'))

    return render(request, 'favorites/view.html', {
        'items_list': favorites_list,
    })


def remove_from_favorites(request):
    if request.POST:
        for key, value in request.POST.items():
            if key.startswith('remove_'):
                # print(f'Key: {key}')
                # print(f'Value: {value}')
                item_id = key[7:]
                # print('item_id', item_id, type(item_id))
                del request.session['favorites'][item_id]
                print('favorites', request.session['favorites'])
                # return redirect(reverse('products:favorites:view'))
    favorites = request.session.get('favorites', {})

    return redirect(reverse('products:favorites:view', {
        'items_list': favorites
    }))
