from django import template

register = template.Library()


@register.filter(name='items_or_names')
def get_items_number_or_name(favorites_dict, filter_type=None):
    if filter_type == 'name':
        products = ''.join([str(product) + '\n' for product in favorites_dict.values()])
        return products
    return len(favorites_dict)


@register.simple_tag(name='favorites_data', takes_context=True)
def get_favorites_data(context):
    fav_dict = context.request.session.get('favorites', {})
    items = ''.join([str(product) + '\n' for product in fav_dict.values()])
    items_number = len(fav_dict)

    return {
        'items': items,
        'number': items_number
    }


@register.filter(name='visible_pages')
def visible_pages(page_obj):
    # print('page_obj', page_obj)  # page_obj <Page 25 of 25>
    paginator = page_obj.paginator
    pages = list(paginator)
    current_page = page_obj.number
    # print('paginator', paginator)  # <django.core.paginator.Paginator object at 0x000002D3D00FAE80>
    # print('current_page', current_page)  # 25
    # for page in paginator:
    #     print('page', page)  # <Page 25 of 25>

    first_pages = pages[0:3]
    last_pages = pages[-3:]
    if current_page in range(1, 7):
        first_pages = pages[0:current_page + 2]
        last_pages = pages[-3:]
        return first_pages + [None] + last_pages
    elif current_page in range(paginator.num_pages - 7, paginator.num_pages + 1):
        last_pages = pages[paginator.num_pages - 10:]
        return first_pages + [None] + last_pages

    current_page_index = [page.number for page in pages].index(current_page)
    return first_pages + [None] + pages[current_page_index - 2:current_page_index + 3] + [None] + last_pages
