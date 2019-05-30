from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from .models import UserProfile

# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = "__all__"
#
#     def clean_avatar(self):
#         avatar = self.cleaned_data['avatar']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), max_length=254, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
