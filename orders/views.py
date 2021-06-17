from django.shortcuts import render, redirect, reverse, Http404
from django.contrib.auth import get_user_model
from orders.models import Order
from django.contrib.auth.decorators import login_required
from products.models import Products
from orders.emails import send_donation_approval_email, send_donation_rejection_email

AuthUserModel = get_user_model()


# Create your views here.
@login_required
def request_product(request, item_id, page_num=None):
    try:
        product = Products.objects.get(id=item_id)
        submitted_orders = Order.objects.filter(user_id=request.user.id)
        requested_prod_ids = [product.item_id for product in submitted_orders]

        # owner should not request their products
        # avoid multiple requests for same product
        # avoid requests on inactive products
        if product.user != request.user and item_id not in requested_prod_ids and product.status < 3:
            order = Order(
                user=request.user,
                item=Products.objects.get(id=item_id),
                owner=product.user
            )
            order.save()
            if product.status == 1:
                product.status = 2
            product.save()

    except Products.DoesNotExist:
        raise Http404('Products with id %s is not available' % item_id)
    # current_url = resolve(request.path_info).url_name
    # if current_url == 'item_view_request_donation':
    #     return redirect(reverse('products:items:item', args=(item_id,)))
    if not page_num:
        previous_url = request.META['HTTP_REFERER']
        return redirect(previous_url)

    return redirect('%s?page=%s' % (
        reverse('products:items:list'),
        page_num
    ))


def requests_orders(request):
    return render(request, 'orders/requests.html')


@login_required
def user_view_requests(request):
    requests = Order.objects.filter(user_id=request.user.id).filter(status=1)  # only active orders
    return render(request, 'orders/donation_requests.html', {
        'requests': requests
    })


@login_required
def owner_view_orders(request):
    try:
        products = Products.objects.filter(user=request.user.id).exclude(status=3)
        product_ids = [product.id for product in products]
        orders = Order.objects.filter(item_id__in=list(product_ids)).filter(status=1)

        return render(request, 'orders/orders.html', {
            'orders': orders,
        })

    except Products.DoesNotExist:
        raise Http404('Products for user %s are not available' % request.user.id)


@login_required
def process_order(request, order_id):
    try:
        # process approved order
        order = Order.objects.get(id=order_id)
        send_donation_approval_email(order.user, order.item.name)
        order.status = 2  # approved
        order.save()

        # process data for other orders for same product
        orders_rejected = Order.objects.filter(item_id=order.item).exclude(id=order_id)
        users_orders_rejected = [order.user for order in orders_rejected]
        if users_orders_rejected:
            send_donation_rejection_email(users_orders_rejected, order.item.name)
        for order in orders_rejected:
            order.status = 3  # rejected
            order.save()

        # process ordered product
        order.item.status = 3  # inactive
        order.item.save()

    except Order.DoesNotExist:
        raise Http404('Order id %s does not exist' % order_id)

    return redirect(reverse('orders:view_orders'))
    pass


@login_required
def cancel_donation_request(request, item_id):
    # get order for user based on prod
    # set order status to cancelled
    # check product status - if no other requests, then set it on active
    pass
