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
    








# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = MyUser
#         fields = '__all__'

#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class LogInForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
#     password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))