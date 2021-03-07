from django.shortcuts import render
from categoreis.models import MotherCategory
from gallery.models import galleryModell
from main.models import IconsModell

def galleryView(request):
    categories = MotherCategory.objects.all()
    gallery = galleryModell.objects.all()
    icons = IconsModell.objects.all()
    context = {
        'categories':categories,
        'gallery':gallery,
        'icons':icons
    }
    return render(request , "gallery.html" , context)




'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''