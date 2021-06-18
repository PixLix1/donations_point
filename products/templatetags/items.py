from django import template
from orders.models import Order

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


@register.simple_tag(name='number_of_requests')
def number_of_requests(item_id):
    nr_requests = Order.objects.filter(item_id=item_id).filter(status=1).count()
    if nr_requests == 1:
        return 'There is 1 active request for this product'
    return 'There are %s active requests for this product' % nr_requests


@register.simple_tag(name='check_user_requests', takes_context=True)
def check_user_requests(item_id, user_id):
    try:
        order = Order.objects.filter(item_id=item_id).filter(user_id=1)

    except Order.DoesNotExist:
        pass
    except IndexError:
        pass


