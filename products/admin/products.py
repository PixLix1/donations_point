from django.contrib import admin
from products.models import Products
from django.utils.html import format_html


# callables
def get_image(obj):
    return format_html('<img src="%s" with="50px" height="50px" />' % obj.image_url)


# set callable names in admin view
get_image.short_description = 'Image'


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', get_image, 'category', 'description', 'status', 'created_at', 'updated_at')
    ordering = ('name', 'status',)
    search_fields = ('name', 'category__name',)
    readonly_fields = ['status']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not request.user.is_superuser:
            return queryset.filter(user=request.user)
        return queryset

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not request.user.is_superuser:
            fields.remove('user')

        return fields

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.user = request.user

        # same thing but only when adding product, not save
        # if not form.cleaned_data.get('user'):
        #     object.user = request.user

        super().save_model(request, obj, form, change)
