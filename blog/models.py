from django.db import models
from django.utils import timezone
#from cloudinary.models import CloudinaryField
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True , null=True)
    #image = models.ImageField(upload_to='media' , null = True)
    #image = models.FileField(upload_to='media')


    def publish(self):
        self.puplished_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')
