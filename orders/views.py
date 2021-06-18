from django.shortcuts import render, redirect, reverse, Http404
from django.contrib.auth import get_user_model
from orders.models import Order
from django.contrib.auth.decorators import login_required
from products.models import Products
from orders.emails import send_donation_approval_email, send_donation_rejection_email, send_product_donated_bulk_email

AuthUserModel = get_user_model()


# Create your views here.
@login_required
def request_product(request, item_id, page_num=None):
    try:
        product = Products.objects.get(id=item_id)
        submitted_orders = Order.objects.filter(status=1).filter(user_id=request.user.id)
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

    previous_url = request.META['HTTP_REFERER']
    if not page_num or 'search_term' in previous_url:
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
def process_order(request, order_id, acceptance):
    try:
        # get data
        order = Order.objects.get(id=order_id)
        other_orders = Order.objects.filter(item_id=order.item).filter(status=1).exclude(id=order_id)
        product = Products.objects.get(id=order.item.id)

        # process approved order
        if acceptance == 1:
            send_donation_approval_email(order.user, order.item.name)
            order.status = 2  # approved
            order.save()

        # process data for other orders for same product
            users_other_orders = [order.user for order in other_orders]
            if users_other_orders:
                send_product_donated_bulk_email(users_other_orders, order.item.name)
            for order in other_orders:
                order.status = 3  # rejected
                order.save()

            # process ordered product
            order.item.status = 3  # inactive
            order.item.save()
        else:
            # process rejected order
            order.status = 3  # rejected
            order.save()
            # process product status - active if no other orders
            if not other_orders:
                product.status = 1
                product.save()
            # inform requestor
            send_donation_rejection_email(order.user, order.item.name)

    except Order.DoesNotExist:
        raise Http404('Order id %s does not exist' % order_id)
    except Products.DoesNotExist:
        raise Http404('Product id does not exist')

    return redirect(reverse('orders:view_orders'))


@login_required
def cancel_donation_request(request, order_id):
    try:
        # get data: order, other active orders same prod and prod
        order = Order.objects.get(id=order_id)
        other_orders = Order.objects.filter(item=order.item.id).filter(status=1).exclude(id=order_id)
        product = Products.objects.get(id=order.item.id)

        # process order - set status to cancelled
        # order excluded from requestor's view by status (only active orders)
        order.status = 6
        order.save()

        # process products - change status to active if no other orders
        if not other_orders:
            product.status = 1
            product.save()

    except Order.DoesNotExist:
        raise Http404('Order %s does not exist' % order_id)
    except Products.DoesNotExist:
        raise Http404('Product id does not exist')
    except IndexError:
        pass

    return redirect(reverse('orders:donation_requests'))
