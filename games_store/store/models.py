from django.conf import settings
from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length = 128)
	thumbnail = models.ImageField(upload_to = 'game_thumbnails/')
	game_files = models.FileField(upload_to ='games/')
	release_date = models.DateTimeField(auto_now_add = True)

	def get_thumbnail_url(self):
		return settings.MEDIA_URL + self.thumbnail.name