from django.urls import path, include
from news import views
urlpatterns = [
    path('', views.News,name='News'),
]