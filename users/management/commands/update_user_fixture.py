import os
import json
from django.core.management import BaseCommand, CommandError


def update_fixture_data(fixture_data):
    print('fixture_data', fixture_data)
    if fixture_data['model'] == 'auth.user':
        fixture_data['model'] = 'users.authuser'
        # del fixture_data['fields']['username']

    return fixture_data


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('--file', '-f', type=str, default=None)
        # parser.add_argument('args', nargs='*')
        # parser.add_argument('-file', '-f', type=str, default=None, nargs='*')

    def handle(self, *args, **options):
        print('print test', options.get('file'))
        file = options.get('file')
        # file = r'D:\Python_ScoalaIT\donations_point\users\fixtures\2021_05_16_data.json'

        if not file:
            raise CommandError('File not provided.')

        if not file.endswith('.json'):
            raise CommandError('Only .json file supported.')

        try:
            with open(file) as json_file:
                fixture_data = json.load(json_file)
        except FileNotFoundError:
            print(file)
            raise CommandError('File not found.')

        fixture_data_map = map(update_fixture_data, fixture_data)
        fixture_data = list(fixture_data_map)

        with open(file, 'w') as json_file:
            json.dump(fixture_data, json_file)
