from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contactus/', contact, name='contact'),
    path('category/<int:category_id>', get_category, name='category'),
    path('view_clothes/<int:collection_id>', view_clothes, name='view_clothes'),
    path('view_clothes/add-clothes/', add_cloth, name='add_cloth')

]
