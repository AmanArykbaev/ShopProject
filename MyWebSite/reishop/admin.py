from django.contrib import admin
from .models import Clothes


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'cloth_name', 'cloth_brand', 'cloth_size', 'cloth_date_release')
    list_display_links = ('id', 'cloth_name', 'cloth_brand')
    search_fields = ('cloth_name', 'cloth_brand', 'cloth_size', 'cloth_date_release')


admin.site.register(Clothes, ShopAdmin)
