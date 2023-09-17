from django.contrib import admin
# from .models  import BestieAdmin
# Register your models here.
# class BestieAdminArea(admin.AdminSite):
#     site_header = 'Bestie Admin Area'

# bestie_admin = BestieAdminArea(name='Bestie Admin')

# bestie_admin.register(BestieAdmin)
from .models import SubUser,BestieAdmin
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    # Customize the fields to display in the admin interface
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_subuser',),
        }),
    )

admin.site.register(SubUser, CustomUserAdmin)
admin.site.register(BestieAdmin)