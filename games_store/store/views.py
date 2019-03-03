from django.shortcuts import render
from django.conf import settings

from .models import Game


def index(request):
	games = Game.objects.all
	return render(request, "store/index.html", {"games": games, "MEDIA_URL": settings.MEDIA_URL })


def detail(request, pk):
	game = Game.objects.get(pk=pk)
	return render(request, "store/detail.html", {"game": game})