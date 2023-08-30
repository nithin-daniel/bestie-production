from django.contrib import admin
from .models import Activity,ClientTestimonials,GalleryPhotos,Packages,Resort,Event
# Register your models here.
admin.site.register(Activity)
admin.site.register(ClientTestimonials)
admin.site.register(GalleryPhotos)
class PackageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"package_slug": ("package_name",)}
admin.site.register(Packages,PackageAdmin)
admin.site.register(Resort)
admin.site.register(Event)