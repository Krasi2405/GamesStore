from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	def is_valid(self):
		if not super(UserRegisterForm, self).is_valid():
			return False

		if User.objects.filter(email=self.cleaned_data["email"]).exists():
			self.add_error("email", "Email already exists!")
			return False

		return True

		

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]


class UserLoginForm(forms.Form):
	username = forms.CharField(label = "Username", max_length = 64)
	password = forms.CharField(label = "Password", max_length = 64, widget = forms.PasswordInput)



class ProfileUpdateForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ["image"]