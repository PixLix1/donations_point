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
