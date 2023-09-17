from django.db import models
from PIL import Image
from django.contrib.auth.models import User,AbstractUser
from main.models import Packages
from django.conf import settings
from django.utils.text import slugify
# Create your models here.


class BestieAdmin(models.Model):
    resort_name = models.CharField(max_length=100)
    resort_description = models.TextField()
    resort_service = models.CharField(max_length=100)
    resort_aminities = models.CharField(max_length=100)
    resort_images = models.ImageField(upload_to='Resort_Image') 
    resort_package = models.ForeignKey(Packages,on_delete=models.CASCADE)
    resort_slug = models.SlugField(blank=True,null=True)
    resort_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    
    
    def save(self, *args, **kwargs):
        if not self.resort_slug:
            self.resort_slug = slugify(self.resort_name)
        super(BestieAdmin, self).save(*args, **kwargs)
    
    
    class Meta:
        verbose_name_plural = 'Resort'
    
    def __str__(self):
        return self.resort_name

class SubUser(AbstractUser):
    is_subuser = models.BooleanField('is_subuser',default=False)
