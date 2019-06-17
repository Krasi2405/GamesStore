from django.contrib.auth.models import User
from rest_framework import serializers
from django.conf import settings
from django.core.files.uploadedfile import UploadedFile
from django.core.files.base import ContentFile


from django.core.files import File
import base64

from store.models import Game, Tag, Platform


class UserSerializer(serializers.HyperlinkedModelSerializer):
    game_set = serializers.PrimaryKeyRelatedField(many=True, queryset=Game.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'game_set')

class ImageSerializerField(serializers.Field):

	def get_attribute(self, instance):
		# We pass the object instance onto `to_representation`,
		# not just the field attribute.
		return instance.thumbnail

	def to_representation(self, value):
		if not value:
			return None

		f = open(value.path, 'rb')
		image = File(f)
		data = base64.b64encode(image.read())
		f.close()

		return data

	def to_internal_value(self, data):
		if isinstance(data, UploadedFile):
			return data
		else:
			format, imgstr = data.split(';base64,') 
			ext = format.split('/')[-1] 

			data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
			return data


class GameSerializer(serializers.HyperlinkedModelSerializer):
	tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())
	platforms = serializers.PrimaryKeyRelatedField(many=True, queryset=Platform.objects.all())


	class Meta:
		model = Game
		fields = ('id', 'name', 'thumbnail', 'description', 'price', 'release_date', 'tags', 'platforms')



class TagSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Tag
		fields = ('id', 'name')


class PlatformSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Platform
		fields = ('id', 'name')