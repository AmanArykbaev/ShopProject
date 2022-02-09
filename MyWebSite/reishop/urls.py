from django.urls import path
from .views import *

urlpatterns = [

    # path('', index, name='home'),
    path('', Home.as_view(), name='home'),
    #path('about/', about, name='about'),
    path('about/', AboutUs.as_view(), name='about'),
    #path('contactus/', contact, name='contact'),
    path('contactus/', ContactUs.as_view(), name='contact'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>', CategoryView.as_view(extra_context={'title': 'Category header'}), name='category'),
    #path('view_clothes/<int:collection_id>', view_clothes, name='view_clothes'),
    path('view_clothes/<int:pk>', ClothView.as_view(), name='view_clothes'),
    #path('view_clothes/add-clothes/', add_cloth, name='add_cloth')
    path('view_clothes/add-clothes/', CreateItem.as_view(), name='add_cloth')

]
