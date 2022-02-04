from django import forms
from .models import *

class ClothForm(forms.ModelForm):
    # cloth_name = forms.CharField(max_length=150, label='Cloth name', required=False,
    #                              widget=forms.TextInput(attrs={"class": "form-control"}))
    #
    # cloth_brand = forms.CharField(label='Brand name', required=False,
    #                               widget=forms.TextInput(attrs={"class": "form-control"}))
    #
    # is_published = forms.BooleanField(label='is published?', initial=True)
    #
    # category = forms.ModelChoiceField(empty_label='Select category', label='Category', queryset= Category.objects.all(),
    #                                   widget=forms.Select())
    class Meta:
        model = Clothes
        fields = ['cloth_name', 'cloth_brand', 'is_published', 'photo', 'category']
        #fields = '__all__'

        # widgets = {'cloth_name': forms.TextInput(attrs={"class": "form-control"}),
        #            'cloth_brand': forms.TextInput(attrs={"class": "form-control"}),
        #            'category': forms.Select(attrs={"class": "form-control"}),
        #            }


