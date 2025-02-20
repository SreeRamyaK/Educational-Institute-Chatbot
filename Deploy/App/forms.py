from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import custom_user, user_personal_model, staff_database


class Reg_form(UserCreationForm):
    class Meta:
        model = custom_user
        fields = ('username', 'email', 'password1', 'password2', 'is_staff', 'is_student')

class user_personal_form(forms.ModelForm):
    class Meta:
        model = user_personal_model
        fields = ['user', 'firstname', 'lastname', 'age', 'address','phone','city', 'state','country','registration_flag']


class staff_personal_form(forms.ModelForm):
    class Meta:
        model = staff_database
        fields = ['user', 'imagefile', 'year', 'post', 'department','school']
