from django.contrib import admin
from .models import Activity,ClientTestimonials,GalleryPhotos,GalleryCategory,ResortName,ResortCategory
# Register your models here.
admin.site.register(Activity)
admin.site.register(ClientTestimonials)
admin.site.register(GalleryPhotos)
admin.site.register(ResortName)
admin.site.register(ResortCategory)