import requests
import os
from donations_point.settings import MEDIA_ROOT
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


USER_FIELDS = ['username', 'email', 'first_name', 'last_name']


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    fields = dict(
        (name, kwargs.get(name, details.get(name)))
        for name in backend.setting('USER_FIELDS', USER_FIELDS)
    )
    if not fields:
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields, is_social_auth=True),
    }


def get_profile_picture(backend, user, response, is_new, **kwargs):
    url = None
    params = {}

    if backend.name == 'google-oauth2':
        url = response.get('picture')
    elif backend.name == 'facebook':
        url = 'https://graph.facebook.com/%s/picture?access_token=%s' % (
            response['id'],
            response['access_token']
        )

    params['type'] = 'large'

    if url:
        try:
            image_request = requests.request('GET', url, params=params)
            image_request.raise_for_status()
        except requests.HTTPError:
            pass
        else:
            old_image_name = str(user.profile.avatar).replace('/', '\\')
            img_path = os.path.join(MEDIA_ROOT, old_image_name)
            default_storage.delete(img_path)
            image_content = image_request.content
            profile = user.profile
            profile.avatar.save('%s.jpg' % user.id, ContentFile(image_content))
            profile.save()


