import os
import json
from django.core.management import BaseCommand, CommandError
from products.models import Products
from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str, default=None)

    def handle(self, *args, **options):
        file_path = options.get('file')

        if not file_path:
            raise CommandError('File not provided.')

        if not file_path.endswith('.json'):
            raise CommandError('Only .json file supported.')

        file_path = os.path.join('data', file_path)
        try:
            with open(file_path) as import_file:
                products = json.load(import_file)
        except FileNotFoundError as e:
            raise CommandError('File at %s was not found' % os.path.join('data', file_path))

        # user = AuthUserModel.objects.filter(id=product['user_id']).first()
        # print(user.first_name)

        for product in products:
            # print(product['user_id'])
            # user = AuthUserModel.objects.filter(id=product['user_id']).first()
            # print(user.first_name)
            db_product = Products(
                category=product['category'],
                name=product['name'],
                description=product['description'],
                image_url=product['image_url'],
                # user_id=AuthUserModel.objects.filter(id=product['user_id']).first()
                user_id=product['user_id']
            )
            db_product.save()
