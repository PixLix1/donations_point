from products.models import Products, Favorites as FavoritesModel
import json


class Favorites:
    def __init__(self, user, session):
        self._user = user
        self._session = session
        self._data = session.get('favorites', {})

    def add(self, item_id):
        item_id_key = str(item_id)
        product = Products.objects.get(pk=item_id)
        self._data[item_id_key] = product.name
        self._save()

    def remove(self, item_id):
        item_id_key = str(item_id)
        del self._data[item_id_key]
        self._save()

    def _save(self):
        try:
            favorites_model = FavoritesModel.objects.get(user=self._user)
            favorites_model.data = json.dumps(self._data)
        except FavoritesModel.DoesNotExist:
            favorites_model = FavoritesModel(user=self._user, data=json.dumps(self._data))
        favorites_model.save()
        self._session['favorites'] = self._data

    @staticmethod
    def load(user, session):
        try:
            favorites_model = FavoritesModel.objects.get(user=user)
            favorites_data = json.loads(favorites_model.data)
        except FavoritesModel.DoesNotExist:
            favorites_data = {}

        session['favorites'] = favorites_data

