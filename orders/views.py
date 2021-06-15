from django.shortcuts import render, redirect, reverse, Http404
from django.contrib.auth import get_user_model
from orders.models import Order
from django.contrib.auth.decorators import login_required
from products.models import Products

AuthUserModel = get_user_model()


# Create your views here.
@login_required
def request_product(request, item_id):
    try:
        product = Products.objects.get(id=item_id)
        submitted_orders = Order.objects.filter(user_id=request.user.id)
        requested_prod_ids = [product.item_id for product in submitted_orders]

        # owner should not request their products
        # avoid multiple requests for same product
        # avoid requests on inactive products
        if product.user != request.user and item_id not in requested_prod_ids and product.status != 3:
            order = Order(
                user=request.user,
                item=Products.objects.get(id=item_id)
            )
            order.save()
            if product.status != 2:
                product.status = 2
                product.save()

    except Products.DoesNotExist:
        raise Http404('Products with id %s is not available' % item_id)
    except Order.DoesNotExist:
        pass

    return redirect(reverse('products:items:list'))


def get_orders(request):
    return render(request, 'orders/requests.html')


@login_required
def owner_view_orders(request):
    try:
        products = Products.objects.filter(user=request.user.id)
        product_ids = [product.id for product in products]
        orders = Order.objects.filter(item_id__in=list(product_ids))

        requests = Order.objects.filter(user_id=request.user.id)

        return render(request, 'orders/orders.html', {
            'orders': orders,
            'requests': requests,
        })

    except Products.DoesNotExist:
        raise Http404('Products for user %s are not available' % request.user.id)

    # if products:
    #     product_ids = [product.id for product in products]
    #     orders = Order.objects.filter(item_id__in=list(product_ids))

        # return render(request, 'orders/orders.html', {
        #     'orders': orders
        # })

    # return render(request, 'orders/orders.html')
