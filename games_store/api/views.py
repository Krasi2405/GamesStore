from django.contrib.auth.models import User

from store.models import Game, Tag, Platform

from rest_framework import viewsets
from .serializers import UserSerializer, GameSerializer, TagSerializer, PlatformSerializer





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