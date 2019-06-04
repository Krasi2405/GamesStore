from django.contrib.auth.models import User
from rest_framework import serializers

from django.core.files import File
import base64

from store.models import Game, Tag, Platform


class UserSerializer(serializers.HyperlinkedModelSerializer):
    game_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'game_set')


class GameSerializer(serializers.HyperlinkedModelSerializer):
	tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
	platforms = serializers.PrimaryKeyRelatedField(many=True, queryset=Platform.objects.all())

	thumbnail_download = serializers.SerializerMethodField(allow_null=True, read_only=True)

	def get_thumbnail(self, obj):
		if not obj.thumbnail:
			return None

		f = open(obj.thumbnail.path, 'rb')
		image = File(f)
		data = base64.b64encode(image.read())
		f.close()
		return data

	class Meta:
		model = Game
		fields = ('id', 'name', 'thumbnail', 'thumbnail_download', 'description', 'price', 'release_date', 'tags', 'platforms')


class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'name')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Platform
		fields = ('id', 'name')