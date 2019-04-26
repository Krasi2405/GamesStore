from django.contrib import admin

from . import models
# Register your models here.

class GameImageInline(admin.TabularInline):
	model = models.GameImage
	extra = 3


class ReviewInline(admin.TabularInline):
	model = models.Review
	extra = 3


class GameAdmin(admin.ModelAdmin):
	list_display = ('name',)
	inlines = [GameImageInline, ReviewInline]


admin.site.register(models.Game, GameAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Review)
admin.site.register(models.Platform)