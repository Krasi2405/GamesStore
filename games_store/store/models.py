from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length = 128)
	description = models.TextField()
	price = models.IntegerField()
	thumbnail = models.ImageField(upload_to = 'game_thumbnails/')
	takes_two_columns = models.BooleanField(default=False)
	game_files = models.FileField(upload_to ='games/')
	release_date = models.DateTimeField(auto_now_add = True)
	tags = models.ManyToManyField('Tag')
	platforms = models.ManyToManyField('Platform')
	owners = models.ManyToManyField(User)

	def get_thumbnail_url(self):
		return settings.MEDIA_URL + self.thumbnail.name

	def __str__(self):
		return self.name


class GameImage(models.Model):
	game = models.ForeignKey('Game', on_delete = models.CASCADE)
	image = models.ImageField(upload_to = 'game_images/')

	def get_url(self):
		return settings.MEDIA_URL + self.image.name


class Review(models.Model):
	game = models.ForeignKey('Game', on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	title = models.CharField(max_length = 128)
	rating = models.IntegerField()
	description = models.TextField()

	def __str__(self):
		return "review for {} by {}: {}".format(self.game.name, self.user.username, self.title)


class Tag(models.Model):
	name = models.CharField(max_length = 32)

	def __str__(self):
		return self.name


class Platform(models.Model):
	name = models.CharField(max_length = 32)

	def __str__(self):
		return self.name