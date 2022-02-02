from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    allItems = Clothes.objects.all()
    categories = Category.objects.all()
    content = {'items': allItems,
               'titleInHtml': 'All Shop Items',
               'categories': categories
               }
    return render(request, template_name="reishop/index.html", context=content)


def get_category(request, category_id):
    item = Clothes.objects.filter(category=category_id)
    categories = Category.objects.order_by('cloth_name')
    category = Category.objects.get(pk=category_id)
    content = {'item': item,
               'allCategories': categories,
               'category': category
               }
    return render(request, "reishop/category.html", content)


def about(request):
    return render(request, "reishop/aboutus.html")


def contact(request):
    return render(request, "reishop/contactus.html")
