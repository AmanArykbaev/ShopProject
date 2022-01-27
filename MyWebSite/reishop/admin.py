from django.contrib import admin
from .models import *


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'cloth_name', 'cloth_brand', 'cloth_size', 'cloth_date_release', 'category', 'is_published')
    list_display_links = ('id', 'cloth_name', 'cloth_brand')
    search_fields = ('cloth_name', 'cloth_brand', 'cloth_size', 'cloth_date_release', 'category')
    list_filter = ('cloth_date_release', 'is_published', 'category')
    list_editable = ('is_published',)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cloth_name')
    list_display_links = ('id', 'cloth_name')
    search_fields = ('cloth_name',)


admin.site.register(Clothes, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
