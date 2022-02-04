from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        max_length=200,
        help_text='Required',
        widget=forms.TextInput(attrs={
            'placeholder': "Enter Your emailaddress",
            'type': "text",
            'id': "email",
            'class':'block w-full px-4 py-4 mt-2 text-xl placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-600 focus:ring-opacity-50'
            }))
    phone_no = forms.CharField(
        max_length=200,
        help_text='Required',
        widget=forms.TextInput(attrs={
            'placeholder': "Enter Your phone number",
            'type': "text",
            'id': "mobile",
            'class':'block w-full px-4 py-4 mt-2 text-xl placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-600 focus:ring-opacity-50'
            }))

    accountType = forms.ChoiceField(
        choices=[('1', 'Individual'), ('2', 'Corporate')],
        widget=forms.RadioSelect(attrs={
            'id': "accountType",
            'class':'inline-flex items-center'
            }))
    password1 = forms.CharField(
        max_length=200,
        help_text='Required',
        widget=forms.PasswordInput(attrs={
            'placeholder': "Enter Your password",
            'type': "password",
            'id': "password",
            'class':'block w-full px-4 py-4 mt-2 text-xl placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-600 focus:ring-opacity-50'
            }))
    password2 = forms.CharField(
        max_length=200,
        help_text='Required',
        widget=forms.PasswordInput(attrs={
            'placeholder': "Enter Your password again",
            'type': "password",
            'id': "password2",
            'class':'block w-full px-4 py-4 mt-2 text-xl placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-600 focus:ring-opacity-50'
            }))
    


    class Meta:
        model = User
        fields = ('phone_no', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    phone_no = forms.CharField(
        max_length=200,
        help_text='*',
        widget=forms.TextInput(attrs={
            'placeholder': "Enter Your phone number",
            'type': "text",
            'id': "mobile",
            'class':'block w-full px-4 py-4 mt-2 text-xl placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-600 focus:ring-opacity-50'
            }))
    password = forms.CharField(
        max_length=200,
        help_text='*',
        widget=forms.PasswordInput(attrs={
            'placeholder': "Enter Your password",
            'type': "password",
            'id': "password",
            'class':'block w-full px-4 py-4 mt-2 text-xl placeholder-gray-400 bg-gray-200 rounded-lg focus:outline-none focus:ring-4 focus:ring-blue-600 focus:ring-opacity-50'
            }))

    class Meta: 
        fields = ('phone_no', 'password')
