from django.db import models

class NewsModell(models.Model):
    Title = models.CharField(max_length=255,verbose_name='News Title')
    Discraptions = models.TextField(max_length=700,verbose_name='News Discraptions')
    Image = models.ImageField(max_length=700,verbose_name='News Image')
    NewsLink = models.CharField(max_length=1000,verbose_name='News Link')
    Date = models.DateTimeField()

    def __str__(self):
        return self.Title
    class Meta():
        verbose_name_plural = 'News Model'
