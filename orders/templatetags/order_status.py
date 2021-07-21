from django import template

register = template.Library()


@register.filter(name='orders_by_status')
def get_orders_by_status(orders, filter_type=None):
    active_orders = []
    if filter_type == 'active':
        for order in orders:
            if order.status == 1:
                active_orders += order
        return active_orders

