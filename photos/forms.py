from django import forms
from .models import Photos


class Uploaded(forms.ModelForm):

    class Meta:
        model = Photos
        fields = '__all__'
