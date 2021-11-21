from django.contrib import admin
from . import models


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'videoId', 'title', 'image', 'channelTitle', 'isFavorite')
