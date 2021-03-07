from django import forms 
from .models import ContactModel



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        exclude = ('Date',)
        widgets = {
            'Name': forms.TextInput(attrs={'class':'form-control','placeholder':"الإسم.."}),
            'Email': forms.EmailInput(attrs={'class':'form-control','placeholder':"البريد الالكتروني.."}),
            'Subject': forms.TextInput(attrs={'class':' form-control','placeholder':"موضوع الرسالة.."}),
            'Message': forms.Textarea(attrs={'class':'form-control','placeholder':"الرسالة.."}),
        }
