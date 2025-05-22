from django import forms
from .models import Wheel, WheelItem

class WheelForm(forms.ModelForm):
    class Meta:
        model = Wheel
        fields = ['name']

class WheelItemForm(forms.ModelForm):
    class Meta:
        model = WheelItem
        fields = ['text', 'weight', 'color']
        widgets = {
            'color': forms.TextInput(attrs={'type': 'color'}),
        }