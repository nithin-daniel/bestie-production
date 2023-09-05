from django.db import models
from PIL import Image
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




    def __str__(self):
        return self.category_name
    
    
class GalleryPhotos(models.Model):
    gallery_image = models.ImageField(upload_to='gallery_photos')
    class Meta:
        verbose_name_plural = 'Gallery Photos'

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
    resort_name = models.CharField(max_length=100)
    resort_description = models.TextField()
    resort_service_1 = models.CharField(max_length=100)
    resort_service_2 = models.CharField(max_length=100)
    resort_service_3 = models.CharField(max_length=100)
    resort_service_4 = models.CharField(max_length=100)
    resort_service_5 = models.CharField(max_length=100)
    resort_service_6 = models.CharField(max_length=100)
    resort_service_7 = models.CharField(max_length=100)
    resort_service_8 = models.CharField(max_length=100)
    resort_aminities_1 = models.CharField(max_length=100)
    resort_aminities_2 = models.CharField(max_length=100)
    resort_aminities_3 = models.CharField(max_length=100)
    resort_aminities_4 = models.CharField(max_length=100)
    resort_aminities_5 = models.CharField(max_length=100)
    resort_aminities_6 = models.CharField(max_length=100)
    resort_aminities_7 = models.CharField(max_length=100)
    resort_aminities_8 = models.CharField(max_length=100)
    resort_amount  = models.CharField(max_length=100)
    resort_images = models.ImageField(upload_to='Resort_Image') 
    resort_package = models.ForeignKey(Packages,on_delete=models.CASCADE)
    resort_slug = models.SlugField()
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


class LatestNews(models.Model):
    news_title = models.CharField(max_length=100)
    news_date = models.DateField()
    news_description = models.TextField()
    new_image = models.ImageField(upload_to='New Imges/')

    class Meta:
        verbose_name_plural = 'Latest News'

    def __str__(self):
        return self.news_title
    
    
    
