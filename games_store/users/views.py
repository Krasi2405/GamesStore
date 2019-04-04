from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import UserRegisterForm

def register(request):
	form = UserRegisterForm()

	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save() # Saves user. Django ftw!

			username = form.cleaned_data.get("username")
			messages.success(request, "Account created! Please log in using your account information.".format(username))
			return redirect("/users/login")
		else:
			messages.error(request, "Account creation failed!")


	return render(request, "users/register.html", {"form": form})