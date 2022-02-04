from django import template

from reishop.models import Category

register = template.Library()

@register.simple_tag(name='categoryFind')
def find_category():
    return Category.objects.all()