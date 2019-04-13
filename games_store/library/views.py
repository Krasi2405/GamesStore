import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse

from store.models import Game

@login_required
def index(request):
	games = Game.objects.all().filter(owners=request.user)
	print(games)
	return render(request, "library/index.html", {"games": games})


@login_required
def download(request, pk):
	game = Game.objects.get(pk=pk)
	file_path = os.path.basename(game.game_files.name)
	print("file path {}".format(file_path))
	response = HttpResponse(game.game_files)
	response["Content-Disposition"] = "attachment; filename={}".format(file_path)
	return response