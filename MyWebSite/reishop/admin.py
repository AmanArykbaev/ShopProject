from django.contrib import admin
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ShopAdminForm(forms.ModelForm):
    cloth_name = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Clothes
        fields = '__all__'


class ShopAdmin(admin.ModelAdmin):
    form = ShopAdminForm
    list_display = (
    'id', 'cloth_name', 'cloth_brand', 'cloth_size', 'cloth_date_release', 'category', 'is_published', 'photo')
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
