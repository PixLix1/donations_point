from django import forms
from django.db import models
from products.models import Category, Products


# order_by_choices = (
#     ('POPULARITY', 'Popularity'),
#     ('PRICE_ASC', 'Price ascending'),
#     ('PRICE_DESC', 'Price descending')
# )


class OrderBy(models.TextChoices):
    # POPULARITY = 'popularity', 'Popularity'
    AVAILABILITY = 'availability', 'Availability'
    # PRICE_ASC = 'price_asc', 'Price ascending'
    # PRICE_DESC = 'price_desc', 'Price descending'


class SearchItems(forms.Form):
    search_term = forms.CharField(max_length=255, required=False, label='Search by name')
    # order_by = forms.ChoiceField(choices=OrderBy.choices, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_filtered_items(self):
        #     # with is_valid Django creates the `cleaned_data` dictionary with all the cleaned informations.
        if self.is_valid():
            search_term = self.cleaned_data.get('search_term', None)
            # items_list = Products.objects.order_by('created_at')
            # if search_term:
            items_list = Products.objects.filter(name__icontains=search_term)
            items_list = items_list.filter(name__icontains=search_term)
            return items_list
        return Products.objects.all()
