from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group, Permission
from products.models import Products, Category
from orders.models import Order
from utils.permissions import get_permission_names
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


class Command(BaseCommand):
    _product_owners_group_name = 'Product Owners'

    @staticmethod
    def _get_product_owners_group():
        try:
            product_owners_group = Group.objects.get(name=Command._product_owners_group_name)
        except Group.DoesNotExist:
            permission_names = get_permission_names([Products, Category, Order])
            permissions = Permission.objects.filter(codename__in=permission_names)
            product_owners_group = Group(name=Command._product_owners_group_name)
            product_owners_group.save()

            product_owners_group.permissions.set(permissions)

        return product_owners_group

    def handle(self, *args, **options):
        product_owners_group = Command._get_product_owners_group()

        try:
            products = Products.objects.all()
            for product in products:
                if len(product.user.groups.filter(name=Command._product_owners_group_name)) == 0:
                    product.user.groups.add(product_owners_group)
        except BaseException as e:
            raise CommandError(e)
