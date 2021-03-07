from django.db import models

class ContactModel(models.Model):
    Name = models.CharField(max_length=250,verbose_name='Name Of User')
    Subject = models.CharField(max_length=350,verbose_name='Subject Of User')
    Email  = models.EmailField(max_length=350,verbose_name='Email Of User')
    Message  = models.TextField(max_length=1000,verbose_name='Message Of User')
    Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.Name) + str(" < | > ") + str(self.Email)



'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''