from django import forms



class LogInForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)


class NewCustomUser(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput())
    display_name = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=100)
    homepage = forms.URLField(required=False)
    age = forms.IntegerField(widget=forms.NumberInput())
    email = forms.EmailField()
    








