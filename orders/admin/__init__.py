from django.contrib import admin
from orders.models import Order
from django.utils.html import format_html


# callables
def get_requestor_full_name(obj):
    return '%s %s' % (obj.user.first_name, obj.user.last_name)


def get_product_name(obj):
    return obj.item.name


def get_image(obj):
    return format_html('<img src="%s" with="50px" height="50px" />' % obj.item.image_url)


# set callables names in admin view
get_requestor_full_name.short_description = 'Requestor name'
get_product_name.short_description = 'Product name'
get_image.short_description = 'Image'

# order callable results
# get_product_name.ordering = order.item.name


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', get_product_name, get_image, get_requestor_full_name, 'status', 'created_at', 'updated_at',)
    ordering = ('status', '-created_at',)
    search_fields = ('user_id__first_name', 'user_id__last_name')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            return queryset.filter(owner=request.user)
        return queryset





# # Register your models here.
# admin.site.register(Order)
