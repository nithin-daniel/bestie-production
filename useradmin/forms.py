from django import forms
from django.db.models import fields
from .models import BestieAdmin

class BestieForm(forms.ModelForm):
    class Meta:
        model = BestieAdmin
        fields = ['resort_name','resort_description','resort_service','resort_aminities','resort_images','resort_package']