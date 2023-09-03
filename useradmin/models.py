from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from main.models import Packages
# Create your models here.


class BestieAdmin(models.Model):
    resort_name = models.CharField(max_length=100)
    resort_description = models.TextField()
    resort_service = models.CharField(max_length=100)
    resort_aminities = models.CharField(max_length=100)
    resort_images = models.ImageField(upload_to='Resort_Image') 
    resort_package = models.ForeignKey(Packages,on_delete=models.CASCADE)
    resort_slug = models.SlugField()
    resort_user = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Resort'
    
    def __str__(self):
        return self.resort_name