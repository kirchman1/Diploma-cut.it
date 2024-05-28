from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegForm(UserCreationForm):
    email = forms.EmailField(
        label='Enter Email',
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'someema1l@gmail.com', 'autocomplete': 'off'})
    )
    username = forms.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        label='Enter login',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'somelog1n', 'autocomplete': 'off'})
    )
    password1 = forms.CharField(
        min_length=8,
        label='Enter password',
        required=True,
        help_text='Minimum 8 symbols',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(UserRegForm, self).__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Enter Email',
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    username = forms.CharField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
        label='Enter login',
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )

    class Meta:
        model = User
        fields = ['email', 'username']
