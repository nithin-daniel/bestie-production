from django.contrib import admin
from .models  import BestieAdmin
# Register your models here.
class BestieAdminArea(admin.AdminSite):
    site_header = 'Bestie Admin Area'

bestie_admin = BestieAdminArea(name='Bestie Admin')

bestie_admin.register(BestieAdmin)