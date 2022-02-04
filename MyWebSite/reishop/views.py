from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *


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
    category = Category.objects.get(pk=category_id)
    content = {'item': item,
               'category': category
               }
    return render(request, "reishop/category.html", content)


def about(request):
    return render(request, "reishop/aboutus.html")


def contact(request):
    return render(request, "reishop/contactus.html")


def view_clothes(request, collection_id):
    #collection_item = Clothes.objects.get(pk=collection_id)

    collection_item = get_object_or_404(Clothes, pk=collection_id)
    return render(request, "reishop/view_clothes.html", {'collection_item': collection_item})

def add_cloth(request):
    if request.method == 'POST':
        pass
    else:
        form = ClothForm()
    return render(request, 'reishop/add_cloth.html', {"form": form})
