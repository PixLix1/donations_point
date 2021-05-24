import os
import json
from django.core.management import BaseCommand, CommandError
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
                users = json.load(import_file)
        except FileNotFoundError as e:
            raise CommandError('File at %s was not found' % os.path.join('data', file_path))

        for user in users:
            db_user = AuthUserModel.objects.create_user(
                first_name=user['first_name'],
                last_name=user['last_name'],
                email=user['email'],
                password='python123'
            )
        # print('db_user', db_user)
