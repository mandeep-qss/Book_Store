from django import forms
from Author.models import User

class FormUser(forms.Form):

    sfirstname = forms.CharField(label='sfirstname', max_length=100)
    slastname = forms.CharField(label='slastname', max_length=100)
    semail = forms.CharField(label='semail', max_length=100)
    password = forms.CharField(label='spassword', max_length=100)

class UserInputForm(forms.Form):

    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('password','email')
# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# class SignUpForm(User):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2', )