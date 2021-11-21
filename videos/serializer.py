from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'title', 'image', 'videoId', 'published', 'description', 'channelTitle', 'isFavorite')


class VideoLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'isFavorite')
