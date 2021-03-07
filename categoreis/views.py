from django.shortcuts import render
from .models import MotherCategory , Category , SubCategory , SubMultiCategory 
from main.models import SoundTrack,IconsModell


'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''


# All category views
def CatsView(request):
    categories = MotherCategory.objects.all()
    icons = IconsModell.objects.all()
    context = {
        'categories':categories,
        'icons':icons
    }
    return render(request , "cats/CatsView.html" , context)


# main standerd category views
def menu_categories(request,cats):
    categories = MotherCategory.objects.all()
    category = MotherCategory.objects.get(slug=cats)
    Tracks = Category.objects.filter(parent=category)
    icons = IconsModell.objects.all()
    context = {
            'category':category,
            'Tracks':Tracks,
            'categories':categories,
            'icons':icons
            
        }
    return render(request , "cats/sounds.html" , context)
# sub main category views
def SubCategoryD(request,cats,category_slug):
    categories = MotherCategory.objects.all()
    category_cats = MotherCategory.objects.get(slug=cats)
    category = Category.objects.get(slug=category_slug)
    Tracks = SubCategory.objects.filter(parent=category)
    icons = IconsModell.objects.all()
    context = {
        'categories':categories,
        'Tracks':Tracks,
        'category':category,
        'category_cats':category_cats,
        'icons':icons

    }
    return render(request , "cats/category.html" , context)
# sub of sub main category views
def SubTwoCategoryD(request,cats,category_slug,series_slug):
    categories = MotherCategory.objects.all()
    category_cats = MotherCategory.objects.get(slug=cats)
    category_back = Category.objects.get(slug=category_slug)
    category = SubCategory.objects.get(slug=series_slug)
    Tracks = SubMultiCategory.objects.filter(parent=category)
    icons = IconsModell.objects.all()
    context = {
        'categories':categories,
        'category_cats':category_cats,
        'category_back':category_back,
        'category':category,
        'Tracks':Tracks,
        'icons':icons
    }
    return render(request , "cats/category_Qouran.html" , context)

# sub of sub of sub main category views
def SubMultiCategoryl(request,cats,category_slug,series_slug,sound_slug):
    categories = MotherCategory.objects.all()
    category_cats = MotherCategory.objects.get(slug=cats)
    category_back = Category.objects.get(slug=category_slug)
    category = SubCategory.objects.get(slug=series_slug)
    Track = SubMultiCategory.objects.get(slug=sound_slug)
    sound = SoundTrack.objects.filter(category=Track)
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
    return render(request , "cats/last_cat.html" , context)



