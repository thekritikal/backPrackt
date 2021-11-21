from django.db import models
from django.utils import timezone


class VideoManager(models.Manager):
    def create_video(self, data):
        video = self.create(
            videoId=data["id"],
            title=data["title"],
            image=data["image"],
            description=data["description"],
            published=data["publishTime"],
            channelTitle=data["channelTitle"])
        return video


class Video(models.Model):
    videoId = models.CharField(unique=True, max_length=30)
    title = models.CharField(max_length=100)
    published = models.DateTimeField(default=timezone.now)
    image = models.URLField()
    description = models.CharField(max_length=250)
    channelTitle = models.CharField(max_length=30)
    isFavorite = models.BooleanField(default=False)

    objects = VideoManager()

    def __str__(self):
        return self.title
