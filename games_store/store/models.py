from django.conf import settings
from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length = 128)
	description = models.TextField()
	thumbnail = models.ImageField(upload_to = 'game_thumbnails/')
	game_files = models.FileField(upload_to ='games/')
	release_date = models.DateTimeField(auto_now_add = True)

	def get_thumbnail_url(self):
		return settings.MEDIA_URL + self.thumbnail.name


class GameImage(models.Model):
	game = models.ForeignKey('Game', on_delete = models.CASCADE)
	image = models.ImageField(upload_to = 'game_images/')

	def get_url(self):
		return settings.MEDIA_URL + self.image.name


class Review(models.Model):
	game = models.ForeignKey('Game', on_delete = models.CASCADE)
	user = models.CharField(max_length = 64) # TODO: Create user model
	title = models.CharField(max_length = 128)
	rating = models.IntegerField()
	description = models.TextField()
