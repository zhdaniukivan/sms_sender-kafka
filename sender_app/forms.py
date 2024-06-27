from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = UserCreationForm.Meta.fields + ('email',)
