from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Booking


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',  'first_name', 'last_name',)

class BookingForm(forms.ModelForm):

    check_in = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
    )

    check_out = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
    )
    class Meta:
        model = Booking
        fields = ['check_in', 'check_out', 'room', 'user']
