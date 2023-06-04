from django.db import models

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

class GalleryCategory(models.Model):
    category_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Gallery Category'


    def __str__(self):
        return self.category_name
    
    
class GalleryPhotos(models.Model):
    image_category = models.ForeignKey(GalleryCategory,on_delete=models.CASCADE)
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

class ResortCategory(models.Model):
    category_package = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Resort Category'

    def __str__(self):
        return self.category_package
    
class ResortName(models.Model):
    resort_name = models.CharField(max_length=100)
    resort_category = models.ForeignKey(ResortCategory,on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'Resort Name'

    def __str__(self):
        return self.resort_name
    
