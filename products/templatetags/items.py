from django import template
from products.models import Products

register = template.Library()


@register.filter(name='pagination_url')
def get_pagination_url(request, page_number=1):
    encoded_url = request.GET.urlencode() or ''
    old_page = request.GET.get('page')
    # print('encoded_url', encoded_url)
    # print('old_page', old_page)
    if old_page:
        encoded_url = encoded_url.replace('?', '').replace('page=%s' % old_page, '')
    # print('encoded_url')

    if encoded_url:
        if encoded_url[-1] == '&':
            encoded_url = encoded_url[:-1]
        return '?%s&page=%s' % (encoded_url, page_number)

    return '?page=%s' % page_number


@register.simple_tag(name='item_status', takes_context=True)
def item_status(request, item_id):
    user = request.user
    item = Products.objects.get(pk=item_id)
    # print('user_view', user)
    if item.status == 1:
        return 'Active'
    return 'Requests'
