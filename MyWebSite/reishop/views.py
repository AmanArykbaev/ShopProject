from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class Home(ListView):
    model = Clothes
    template_name = 'reishop/homepage.html'
    context_object_name = 'items'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Cloth Page'
        return context

    def get_queryset(self):
        return Clothes.objects.filter(is_published=True)


class CategoryView(ListView):
    model = Clothes
    template_name = 'reishop/category_view.html'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return Clothes.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ClothView(DetailView):
    model = Clothes
    # pk_url_kwarg = 'collection_id'
    context_object_name = 'collection_item'


class CreateItem(CreateView):
    form_class = ClothForm
    model = Clothes
    template_name = 'reishop/add_new_item.html'
    success_url = reverse_lazy('home')


class AboutUs(ListView):
    model = Clothes
    template_name = 'reishop/about_us_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        return context


class ContactUs(ListView):
    model = Clothes
    template_name = 'reishop/contact_us_page.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        return context

# def index(request):
#     allItems = Clothes.objects.all()
#     content = {'items': allItems,
#                'titleInHtml': 'All Shop Items',
#                }
#     return render(request, template_name="reishop/index.html", context=content)


# def get_category(request, category_id):
#     item = Clothes.objects.filter(category=category_id)
#     category = Category.objects.get(pk=category_id)
#     content = {'item': item,
#                'category': category
#                }
#     return render(request, "reishop/category.html", content)


# def about(request):
#     return render(request, "reishop/aboutus.html")
#
#
# def contact(request):
#     return render(request, "reishop/contactus.html")

# def view_clothes(request, collection_id):
#     # collection_item = Clothes.objects.get(pk=collection_id)
#
#     collection_item = get_object_or_404(Clothes, pk=collection_id)
#     return render(request, "reishop/view_clothes.html", {'collection_item': collection_item})


# def add_cloth(request):
#     if request.method == 'POST':
#         form = ClothForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             Clothes.objects.create(**form.cleaned_data)
#             return redirect('home')
#     else:
#         form = ClothForm()
#     return render(request, 'reishop/add_cloth.html', {"form": form})
