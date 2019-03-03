from django.contrib import admin

from . import models
# Register your models here.

class GameImageInline(admin.TabularInline):
	model = models.GameImage
	extra = 3



class GameAdmin(admin.ModelAdmin):
	list_display = ('name',)
	inlines = [GameImageInline]


admin.site.register(models.Game, GameAdmin)