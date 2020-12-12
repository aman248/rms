from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
    test_name = forms.CharField(max_length=100)

class ShowResultForm(forms.Form):
    rollno = forms.CharField(max_length=100)
    testname = forms.CharField(max_length=100)
    schoolname = forms.CharField(max_length=100)
