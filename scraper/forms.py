from django import forms

class ProfileForm(forms.Form):
    username = forms.CharField(label='Github Username', max_length=100)
