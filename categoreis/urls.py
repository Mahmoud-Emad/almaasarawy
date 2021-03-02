from django.urls import path, include
from . import  views

'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''

# Url Slider Model Above

urlpatterns = [
    path('', views.mainHome,name='homepage'),
    path('cats/', views.CatsView,name='CatsView'),
    path('cats/<slug:cats>/', views.menu_categories,name='sounds'),
    path("cats/<slug:cats>/<slug:category_slug>/", views.SubCategoryD, name="category_blocks"),  
    path("cats/<slug:cats>/<slug:category_slug>/<slug:series_slug>/", views.SubTwoCategoryD, name="subTweo"),  
    path("cats/<slug:cats>/<slug:category_slug>/<slug:series_slug>/<slug:sound_slug>/", views.SubMultiCategoryl, name="SubMultiCategoryl"),  
     
]
