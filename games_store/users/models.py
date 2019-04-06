from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default = "profile_images/default_profile.png", upload_to="profile_images")


	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		print("Create profile!")
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()