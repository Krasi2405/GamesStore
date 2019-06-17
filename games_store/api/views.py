from django.contrib.auth.models import User
from django.core.files import File
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status


from .serializers import UserSerializer, GameSerializer, TagSerializer, PlatformSerializer
from store.models import Game, Tag, Platform

import base64





class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GameViewSet(viewsets.ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer


class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer


class PlatformViewSet(viewsets.ModelViewSet):
	queryset = Platform.objects.all()
	serializer_class = PlatformSerializer



@api_view(['GET'])
def thumbnail_image(request, pk	):
	game = get_object_or_404(Game, pk=pk)
	headers = {
		"type": "image"
	}

	return Response(image_to_b64(game.thumbnail), headers=headers)


def image_to_b64(value):
	if not value:
		return None

	f = open(value.path, 'rb')
	image = File(f)
	data = base64.b64encode(image.read())
	f.close()

	return data