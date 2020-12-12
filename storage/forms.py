from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    file = forms.FileField()
    test_name = forms.CharField(max_length=100)

class ShowResultForm(forms.Form):
    rollno = forms.CharField(max_length=100)
    testname = forms.CharField(max_length=100)
    schoolname = forms.CharField(max_length=100)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
