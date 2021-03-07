from django.shortcuts import redirect, render
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from categoreis.models import MotherCategory
from main.models import IconsModell


def ContactFormView(request):
    form_contact = ContactForm(request.POST)
    categories = MotherCategory.objects.all()
    icons = IconsModell.objects.all()
    if request.method == 'POST':
        subject = request.POST['Subject']
        email = request.POST['Email']
        message = request.POST['Message']
        send_mail(
            f'{subject} from {email}',
            'Some One Wanna To Contact With You \n Message is :\n' + message + '\n' + '\nEmail Is :' + email + '',
            email,
            [settings.EMAIL_HOST_USER],

            )
        if form_contact.is_valid():
            form = ContactForm(request.POST)
            form.save()
            messages.info(request, "” كثيرا من الشكر علي رسالتنك سوف يتم التواصل معك في اقرب وقت ” ")
            return redirect(reverse('homepage'))
    else:
        form = ContactForm()
    context={'form_contact':form_contact,
                'categories':categories,
                'icons':icons
            }
    return render(request,'contact.html',context)



'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''