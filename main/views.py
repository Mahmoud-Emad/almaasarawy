from categoreis.models import MotherCategory,Category,SubCategory,SubMultiCategory
from .models import SoundTrack,IconsModell
from django.shortcuts import render


# Home above

def mainHome(request):
    categories = MotherCategory.objects.all()
    icons = IconsModell.objects.all()
    context = {
        'categories':categories,
        'icons':icons
    }
    return render(request , "HomePage.html" , context)

def SoundCloudDetail(request,cats,category_slug,series_slug,sound_slug,Track_slug):
    categories = MotherCategory.objects.all()
    category_cats = MotherCategory.objects.get(slug=cats)
    category_back = Category.objects.get(slug=category_slug)
    category = SubCategory.objects.get(slug=series_slug)
    Track = SubMultiCategory.objects.get(slug=sound_slug)
    sound = SoundTrack.objects.get(slugTrack=Track_slug)
    Tracks = SubMultiCategory.objects.filter(parent=category)
    Sounds_detail = SubMultiCategory.objects.filter(parent = category)
    icons = IconsModell.objects.all()
    context = {
        'categories':categories,
        'category_cats':category_cats,
        'category_back':category_back,
        'category':category,
        'Tracks':Tracks,
        'Track':Track,
        'sound':sound,
        'Sounds_detail':Sounds_detail,
        'icons':icons
    }
    return render(request , "cat-item.html" , context)



'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''