from django.contrib import admin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ('status')
    pass

# # Register your models here.
# admin.site.register(Order)