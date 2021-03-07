from django.shortcuts import render
from categoreis.models import MotherCategory
from news.models import NewsModell
from main.models import IconsModell

# Create your views here.



def News(request):
    categories = MotherCategory.objects.all()
    News = NewsModell.objects.all()
    icons = IconsModell.objects.all()
    context = {
        'categories':categories,
        'News':News,
        'icons':icons
    }
    return render(request , "news.html" , context)