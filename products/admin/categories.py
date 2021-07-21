from django.contrib import admin
from products.models import Category
from django.utils.html import format_html


# callables
def get_image(obj):
    return format_html('<img src="%s" with="50px" height="50px" />' % obj.image.url)


# set callable names in admin view
get_image.short_description = 'Image'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', get_image, 'created_at', 'updated_at')
    ordering = ('name',)
    search_fields = ('name',)
