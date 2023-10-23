from django.db import models
from PIL import Image
from django.conf import settings
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
import uuid
# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='activity')


    class Meta:
        verbose_name_plural = 'Activity'


    def __str__(self):
        return self.title

class ClientTestimonials(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='MainTestimonials')
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Client Testimonials'


    def __str__(self):
        return self.name

    
    
class GalleryPhotos(models.Model):
    gallery_image = models.ImageField(upload_to='gallery_photos',help_text="Upload only 740x493 pixels image",blank=True)
    gallery_video = models.FileField(upload_to='videos_uploaded',null=True,blank=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    class Meta:
        verbose_name_plural = 'Gallery'

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'

    def __str__(self):
        return self.name
    
class Packages(models.Model):
    package_name = models.CharField(max_length=100)
    package_description = models.TextField()
    package_image = models.ImageField(upload_to='Packages/')
    package_slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.package_image:
            img = Image.open(self.package_image.path)
            target_size = (400, 270)

            # Resize while maintaining aspect ratio
            img.thumbnail(target_size)

            # Calculate cropping dimensions to fit the target size
            width, height = img.size
            left = (width - target_size[0]) / 2
            top = (height - target_size[1]) / 2
            right = (width + target_size[0]) / 2
            bottom = (height + target_size[1]) / 2

            # Crop the image
            img = img.crop((left, top, right, bottom))

            # Save the modified image
            img.save(self.package_image.path)
    class Meta:
        verbose_name_plural = 'Package'
    def __str__(self):
        return self.package_name
    

class Resort(models.Model):
    resort_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    resort_name = models.CharField(max_length=100)
    resort_description = models.TextField()
    resort_service_1 = models.CharField(max_length=100)
    resort_service_2 = models.CharField(max_length=100)
    resort_service_3 = models.CharField(max_length=100,blank=True)
    resort_service_4 = models.CharField(max_length=100,blank=True)
    resort_service_5 = models.CharField(max_length=100,blank=True)
    resort_service_6 = models.CharField(max_length=100,blank=True)
    resort_service_7 = models.CharField(max_length=100,blank=True)
    resort_service_8 = models.CharField(max_length=100,blank=True)
    resort_aminities_1 = models.CharField(max_length=100)
    resort_aminities_2 = models.CharField(max_length=100)
    resort_aminities_3 = models.CharField(max_length=100,blank=True)
    resort_aminities_4 = models.CharField(max_length=100,blank=True)
    resort_aminities_5 = models.CharField(max_length=100,blank=True)
    resort_aminities_6 = models.CharField(max_length=100,blank=True)
    resort_aminities_7 = models.CharField(max_length=100,blank=True)
    resort_aminities_8 = models.CharField(max_length=100,blank=True)
    resort_amount  = models.CharField(max_length=100)
    resort_image_1 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_2 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_3 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_4 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_5 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_6 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_7 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_8 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_9 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_image_10 = models.ImageField(upload_to='Resort_Image',null=True,blank=True) 
    resort_package = models.ForeignKey(Packages,on_delete=models.CASCADE)
    resort_slug = models.SlugField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.resort_slug:
            self.resort_slug = slugify(self.resort_name)
        super(Resort, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Resort'
    
    def __str__(self):
        return self.resort_name
    
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_description = models.TextField()
    event_date = models.DateField()
    event_payment = models.CharField(max_length=100)
    event_specialities = models.CharField(max_length=100)
    event_benefits = models.CharField(max_length=100)
    event_quotes = models.CharField(max_length=100)
    event_photo = models.ImageField(upload_to='Event_Images')
    event_about_section = models.TextField()
    event_no_of_participations = models.PositiveBigIntegerField()

    def __str__(self):
        return self.event_name


class LatestEvents(models.Model):
    news_title = models.CharField(max_length=100)
    news_date = models.DateField()
    news_description = models.TextField()
    new_image = models.ImageField(upload_to='New Imges/')

    class Meta:
        verbose_name_plural = 'Latest Events'

    def __str__(self):
        return self.news_title
    

class Offer(models.Model):
    offer_name = models.CharField(max_length=100)
    offer_desciption = models.CharField(max_length=100,null=True,blank=True)
    offer_date_start = models.DateField()
    offer_start_time = models.TimeField()
    offer_date_end = models.DateField()
    offer_end_time = models.TimeField()
    offer_percentage = models.CharField(max_length=10)
    
    def __str__(self):
        return self.offer_name
    
    
