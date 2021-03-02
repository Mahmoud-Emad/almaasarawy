from django.db import models

class galleryModell(models.Model):
    Image = models.ImageField(max_length=700,verbose_name='News Image')

    def __str__(self):
        return str(self.Image)