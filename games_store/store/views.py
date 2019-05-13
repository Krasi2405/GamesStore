from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.core.paginator import Paginator

from .models import Game, GameImage, Tag, Review

from .forms import ReviewForm

def index(request):
	games = Game.objects.all()
	return render(request, "store/index.html", {"games": games, "MEDIA_URL": settings.MEDIA_URL })


def detail(request, pk):
	game_query = (Game.objects
		.prefetch_related("gameimage_set", "review_set", "tags", "platforms")
	)
	if request.user.is_authenticated:
		game_query.prefetch_related("owenrs")

	game = game_query.get(pk=pk)

	images = game.gameimage_set.all()
	reviews = game.review_set.select_related("user__profile").all()
	tags = game.tags.all()
	platforms = game.platforms.all()

	rating = reviews.aggregate(Avg("rating"))["rating__avg"]

	is_owner = False
	has_reviewed = False
	user_review = None
	review_form = None

	if request.user.is_authenticated:
		if game.owners.filter(id=request.user.pk):
			is_owner = True

		if reviews.filter(user=request.user.pk):
			has_reviewed = True

		if has_reviewed:
			user_review = reviews.get(user=request.user)
		
		review_form = ReviewForm()		
		if request.method == "POST":
			review_form = ReviewForm(request.POST)
			if review_form.is_valid():
				review = Review.objects.create(
					game=game,
					user=request.user,
					title=review_form.cleaned_data["title"],
					rating=review_form.cleaned_data["rating"],
					description=review_form.cleaned_data["description"],
				)
				messages.success(request, "Review added!")
				return redirect("/store/game/" + pk)

	return render(
		request, 
		"store/detail.html", 
		{"game": game, "images": images, "reviews": reviews, "tags": tags, "platforms": platforms,
		 "is_owner": is_owner, "has_reviewed": has_reviewed, "review_form": review_form, 
		 "user_review": user_review, "rating": rating}
	)


def search(request):
	GAMES_PER_PAGE_COUNT = 2

	games_list = Game.objects.all()


	page = 1
	

	if request.GET:
		if request.GET.get("search-text"):
			games_list = games_list.filter(name__contains=request.GET["search-text"])

		if request.GET.get("tags[]"):
			for tag_id in request.GET.getlist("tags[]"):
				games_list = games_list.filter(tags__pk=tag_id)

		if request.GET.get("page"):
			page = request.GET["page"]


	paginator = Paginator(games_list, GAMES_PER_PAGE_COUNT)

	games = paginator.get_page(page)

	tags = Tag.objects.all()

	return render(request, "store/search_bar.html", {"games": games, "tags": tags})


@login_required
def buy(request, game_pk):
	game = Game.objects.get(pk=game_pk)
	game.owners.add(request.user)
	messages.success(request, "Succesfully bought game!")
	return redirect("/store/game/" + game_pk)
