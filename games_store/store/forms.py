from django import forms
from django.contrib.auth.models import User

from .models import Review


class ReviewForm(forms.Form):
	title = forms.CharField(max_length = 64, widget = forms.TextInput(attrs={"placeholder": "Title"}))
	description = forms.CharField(widget = forms.Textarea(
		attrs={"placeholder": "10/10 best game ever",
			   "class": "materialize-textarea"}
	))	
	rating = forms.IntegerField(widget = forms.HiddenInput(attrs={"id": "rating"}))	