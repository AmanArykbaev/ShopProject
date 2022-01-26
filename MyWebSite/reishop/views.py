from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Clothes


def index(request):
    allItems = Clothes.objects.all()
    # res = "<h1>All Shop Items</h1>"

    # for item in allItems:
    #     res += f'<h4>{item.cloth_name}</h4><br><p>{item.cloth_brand}</p>' \
    #            f'<br><br><u>{item.cloth_date_release}</u><hr>'

    return render(request, "reishop/index.html", {'items': allItems, 'titleInHtml': 'All Shop Items'})


def about(request):
    return render(request, "reishop/aboutus.html")


def contact(request):
    return render(request, "reishop/contactus.html")
