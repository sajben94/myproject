from django import forms
from django.core import validators
# from django.contrib.auth.models import User
from myapp.models import Users

def check_email(value):
    if Users.objects.filter(email=value):
        raise forms.ValidationError('You can not use this email address.')

class FormName(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),
                                error_messages={'required': 'Please enter your first name'})

    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),
                                error_messages={'required': 'Please enter your last name'})

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
                             validators=[check_email,])

    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0),])


# class FormUser(forms.Form):
#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     email = forms.EmailField()
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

class FormUser(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
