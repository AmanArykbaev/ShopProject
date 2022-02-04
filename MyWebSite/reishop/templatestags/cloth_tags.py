from django import template

from MyWebSite.reishop.models import Category

register = template.Library()

@register.simple_tag(name='categoryFind')
def find_category():
    return Category.objects.all()