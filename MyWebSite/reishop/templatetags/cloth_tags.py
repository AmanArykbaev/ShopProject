from django import template
from django.db.models import *

from reishop.models import Category, Clothes

register = template.Library()


@register.simple_tag(name='categoryFind')
def find_category():
    allCategories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('clothes')).filter(cnt__gt=0)
    return categories


@register.simple_tag()
def show_categories():
    categories = Category.objects.annotate(cnt=Count('clothes')).filter(cnt__gt=0)
