from django.shortcuts import render
from categoreis.models import MotherCategory
from gallery.models import galleryModell

def galleryView(request):
    categories = MotherCategory.objects.all()
    gallery = galleryModell.objects.all()
    context = {
        'categories':categories,
        'gallery':gallery,
    }
    return render(request , "gallery.html" , context)
