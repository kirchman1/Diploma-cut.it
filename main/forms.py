from django import forms
from .models import Link


class LinkForm(forms.ModelForm):
    link = forms.CharField(
        label='Enter Full URL',
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    slug = forms.CharField(
        label='Enter KEY word',
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )

    class Meta:
        model = Link
        fields = ['link', 'slug']
