from django.shortcuts import render
from categoreis.models import MotherCategory
from news.models import NewsModell

# Create your views here.



def News(request):
    categories = MotherCategory.objects.all()
    News = NewsModell.objects.all()
    context = {
        'categories':categories,
        'News':News,
    }
    return render(request , "news.html" , context)