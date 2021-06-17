from django.contrib import admin
from products.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name')
