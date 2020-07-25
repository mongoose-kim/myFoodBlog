from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

class Picture(models.Model):
    text = models.TextField() 
    image = models.ImageField(upload_to = "blogimg") 
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(130, 130)])
