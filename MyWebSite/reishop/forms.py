from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    fullname = forms.CharField(label='Full Name', widget=forms.TextInput(
        attrs={"class": "form-control"}))
    email = forms.EmailField(label='Email Address', widget=forms.EmailInput(
        attrs={"class": "form-control"}))
    subject = forms.CharField(label='Subject', widget=forms.TextInput(
        attrs={"class": "form-control"}))
    category = forms.ModelChoiceField(empty_label='Select category', label='Category', queryset=Category.objects.all(),
                                      widget=forms.Select(), required=False)
    content = forms.CharField(label='Your question', widget=forms.Textarea(
        attrs={"class": "form-control", "rows": 10}))


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={"class": "form-control", "autocomplete": "off"}))

    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={"class": "form-control"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={"class": "form-control", "autocomplete": "off"}))

    email = forms.EmailField(label='Email:', widget=forms.EmailInput(
        attrs={"class": "form-control"}))

    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


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
        # fields = '__all__'

        # widgets = {'cloth_name': forms.TextInput(attrs={"class": "form-control"}),
        #            'cloth_brand': forms.TextInput(attrs={"class": "form-control"}),
        #            'category': forms.Select(attrs={"class": "form-control"}),
        #            }
