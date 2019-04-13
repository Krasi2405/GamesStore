from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm

from store.models import Review, Game

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


def login_view(request):
	form = UserLoginForm()

	if request.method == "POST":
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")

			user = User.objects.filter(email=username)
			if user:
				user = user[0]
				return authenticate_user(request, user.username, password)
				
			user = User.objects.filter(username=username)
			if user:
				user = user[0]
				return authenticate_user(request, username, password)

			messages.error(request, "User doesn't exist!")

	return render(request, "users/login.html", {"form": form})


def authenticate_user(request, username, password):
	user = authenticate(request, username=username, password=password)
	if user:
		login(request, user)
		messages.success(request, "Succesfully logged in!")
		return redirect("/store/")
	else:
		messages.error(request, "Username or password are incorrect!")
		form = UserLoginForm(request.POST)
		return render(request, "users/login.html", {"form": form})



def profile(request, pk):
	user = User.objects.get(pk=pk)
	profile = user.profile

	is_profile_owner = (user.pk == request.user.pk)

	reviews = Review.objects.filter(user=user)
	games = Game.objects.filter(owners=user)
	update_form = None
	if is_profile_owner:
		print("Gotten request form")
		update_form = ProfileUpdateForm(instance=request.user.profile)
		if request.method == "POST":
			update_form = ProfileUpdateForm(
				request.POST, 
				request.FILES, 
				instance=request.user.profile
			)
			if update_form.is_valid():
				update_form.save()
				messages.success(request, "Succesfully updated account!")
				return redirect("/users/profile/" + pk)
			else:
				messages.error(request, "Account update failed!")


	return render(request, "users/profile.html", 
			{"profile": profile, 
			 "is_profile_owner": is_profile_owner,
			 "update_form": update_form,
			 "reviews": reviews,
			 "games": games}
	)

