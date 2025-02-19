from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
