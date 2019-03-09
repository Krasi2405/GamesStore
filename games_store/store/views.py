from django.shortcuts import render
from django.conf import settings

from .models import Game, GameImage, Tag


def index(request):
	games = Game.objects.all()
	return render(request, "store/index.html", {"games": games, "MEDIA_URL": settings.MEDIA_URL })


def detail(request, pk):
	game = Game.objects.get(pk=pk)
	images = game.gameimage_set.all()
	reviews = game.review_set.all()
	tags = game.tags.all()
	return render(
		request, 
		"store/detail.html", 
		{"game": game, "images": images, "reviews": reviews, "tags": tags}
	)

def search(request):
	games = Game.objects.all()
	print(request.GET)

	if request.GET:
		if request.GET.get("search-text"):
			games = games.filter(name__contains=request.GET["search-text"])
		if request.GET.get("tags[]"):
			for tag_id in request.GET.getlist("tags[]"):
				games = games.filter(tags__pk=tag_id)



	tags = Tag.objects.all()

	return render(request, "store/search_bar.html", {"games": games, "tags": tags})