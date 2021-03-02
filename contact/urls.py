from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.ContactFormView,name='contact'),
]