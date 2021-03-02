from django.db import models
import random
import string 
from django.utils.text import slugify
from django.contrib.auth.models import User


'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''

choice_list = (
    ('Category Page','Category Page'),
    ('Sound Cloud Track','Sound Cloud Track'),
    ('YouTube Video','YouTube Video'),
)



class MotherCategory(models.Model):
    Title = models.CharField(max_length=255,verbose_name='Category Title')
    TitleEnglish = models.CharField(max_length=255,verbose_name='English Category Title')
    slug = models.SlugField(max_length=255,null=True,blank=True,verbose_name='Let this field empty', unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.TitleEnglish))
        super(MotherCategory,self).save(*args, **kwargs)  

    def __str__(self): 
        return self.Title                      
    
    class Meta:
        verbose_name_plural             =                       "1st Main Categoreis"  

class Category(models.Model):
    parent = models.ForeignKey('MotherCategory',related_name='children_one',on_delete=models.CASCADE,verbose_name='Category Of')
    Title = models.CharField(max_length=255,verbose_name='Category Title')
    TitleEnglish = models.CharField(max_length=255,verbose_name='English Category Title')
    slug = models.SlugField(max_length=255,null=True,blank=True,verbose_name='Let this field empty', unique=True)
    IsBook = models.BooleanField(max_length=255,default=False,verbose_name='This is Book Or Page Link?')
    BookLink = models.CharField(max_length=255,verbose_name='Put Link Here',null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.TitleEnglish))
        super(Category,self).save(*args, **kwargs)   
    
    def GetFoub(self):
        return(self.LinkEmbed).replace('ell','qq')  

    def __str__(self):                           
        return self.Title

    class Meta:
        verbose_name_plural             =                       "2nd Mother Categoreis" 


class SubCategory(models.Model):
    parent = models.ForeignKey('Category',related_name='children_two',on_delete=models.CASCADE,verbose_name='Category Of')
    Title = models.CharField(max_length=255,verbose_name='Category Title')
    TitleEnglish = models.CharField(max_length=255,verbose_name='English Category Title')
    slug = models.SlugField(max_length=255,null=True,blank=True,verbose_name='Let this field empty', unique=True)
    IsTrack = models.BooleanField(default=False,null=True,blank=True,verbose_name='This is link ? if this is link please write it above')
    TrackLink = models.CharField(max_length=255,null=True,blank=True,verbose_name='You will definitely write it here')
    Chicese_list = models.CharField(max_length=255,choices=choice_list,default='Category Page',verbose_name='Choice What is it')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.TitleEnglish))
        super(SubCategory,self).save(*args, **kwargs)  
    
    def YouTubeVideoEmbed(self):
        return(self.TrackLink).replace('watch?v=','embed/')
    def SoundTrackEmbed(self):
        return(self.TrackLink[0:173]).replace('<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="','')

    def __str__(self):                           
        return self.Title

    class Meta:
        verbose_name_plural             =                       "3rd Child Categoreis" 

class SubMultiCategory(models.Model):
    parent = models.ForeignKey('SubCategory',related_name='children_Three',on_delete=models.CASCADE,verbose_name='Category Of')
    Title = models.CharField(max_length=255,verbose_name='Category Title')
    TitleEnglish = models.CharField(max_length=255,verbose_name='English Category Title')
    slug = models.SlugField(max_length=255,null=True,blank=True,verbose_name='Let this field empty', unique=True)
    Chicese_list = models.CharField(max_length=255,choices=choice_list,default='Category Page',verbose_name='Choice What is it')
    TrackLink = models.CharField(max_length=10000,verbose_name='Track Link',null=True,blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.TitleEnglish)+ '-id-' + str(self.id))
        super(SubMultiCategory,self).save(*args, **kwargs) 
    class Meta:
        verbose_name_plural             =                       "4th Child Categoreis"
    def __str__(self):                           
        return (self.Title)  
    def YouTubeVideoEmbed(self):
        return(self.TrackLink).replace('watch?v=','embed/')   
    def SoundTrackEmbed(self):
        return(self.TrackLink[0:173]).replace('<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="','')

