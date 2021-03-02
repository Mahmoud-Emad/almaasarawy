from django.urls import path, include
from . import  views



urlpatterns = [
    path("cats/<slug:cats>/<slug:category_slug>/<slug:series_slug>/<slug:sound_slug>/<slug:Track_slug>/", views.SoundCloudDetail, name="SoundCloudDetail"), 
     
]