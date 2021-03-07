from django.db import models
from django.contrib.auth.models import User
from categoreis.models import SubMultiCategory
from django.utils.text import slugify
Tracks = (
    ('Sound Cloud Track','Sound Cloud Track'),
    ('YouTube Video','YouTube Video'),
)


class SoundTrack(models.Model):
    Title = models.CharField(max_length=255,verbose_name='Item Title')
    TitleEnglish = models.CharField(max_length=255,verbose_name='English Item Title')
    category = models.ForeignKey(SubMultiCategory,related_name='Tracks',on_delete=models.CASCADE)
    Chicese_list = models.CharField(max_length=255,choices=Tracks,verbose_name='Choice What is it')
    TrackLink = models.CharField(max_length=10000,verbose_name='Item Link')
    slugTrack = models.SlugField(max_length=255,null=True,blank=True,verbose_name='Let this field empty', unique=True)

    def __str__(self): 
        return '( ' + self.Title + ' من ( ' + str(self.category)
    def save(self, *args, **kwargs): 
        self.slugTrack = slugify(str(self.TitleEnglish) + str(self.TrackLink[7:22]) + '-id-' + str(self.id))
        print(self.id)
        super(SoundTrack,self).save(*args, **kwargs)
    def YouTubeVideoEmbed(self):
        return(self.TrackLink).replace('watch?v=','embed/')   
    def SoundTrackEmbed(self):
        cut  = self.TrackLink[88:]
        get = cut[0:86]
        return get
    class Meta:
        verbose_name_plural             =                       "Sounds And Youtube"  


Icons_Selct = (
    ('Facebook Icon','Facebook Icon'),
    ('YouTube Icon','YouTube Icon'),
    ('SoundCloud Icon','SoundCloud Icon'),
    ('Twitter Icon','Twitter Icon'),
    ('Insta Icon','Insta Icon'),
    ('Telegram Icon','Telegram Icon'),
)
class IconsModell(models.Model):
    Chicese_list = models.CharField(max_length=255,choices=Icons_Selct,verbose_name='Choice What is it')
    Link = models.CharField(max_length=255,verbose_name='Link Is')
    
    def __str__(self): 
        return str(self.Chicese_list)
    class Meta:
        verbose_name_plural             =                       "Social Media Icons"  



'''
    .__(.)< (MEOW)
    \___)
~~~~~~~~~~~~~
    --Mahmoud Emad

'''