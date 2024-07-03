from django import forms
from .models import Image

class Imageform(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'  # Or specify the fields you want to include
        labels = {'photo':''}
