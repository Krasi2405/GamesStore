from django.shortcuts import render
from django.conf import settings

from .models import Game, GameImage


def index(request):
	games = Game.objects.all
	return render(request, "store/index.html", {"games": games, "MEDIA_URL": settings.MEDIA_URL })


def detail(request, pk):
	game = Game.objects.get(pk=pk)
	images = game.gameimage_set.all()
	return render(request, "store/detail.html", {"game": game, "images": images})