from django.contrib import admin
from .models import Activity,ClientTestimonials,GalleryPhotos,Packages,Resort,Event,LatestEvents,ContactUs,Offer
# Register your models here.
admin.site.register(Activity)
admin.site.register(ClientTestimonials)
admin.site.register(GalleryPhotos)
class PackageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"package_slug": ("package_name",)}
admin.site.register(Packages,PackageAdmin)
class ResortAdmin(admin.ModelAdmin):
    prepopulated_fields = {"resort_slug": ("resort_name",)}
admin.site.register(Resort,ResortAdmin)
admin.site.register(Event)
# admin.site.register(LatestEvents)
admin.site.register(ContactUs)
admin.site.register(Offer)