import json
from .serializer import VideoSerializer, VideoLikeSerializer
from .models import Video
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
import requests
from django.conf import settings


YOUTUBE_KEY1 = settings.YOUTUBE_KEY1
YOUTUBE_KEY2 = settings.YOUTUBE_KEY2
YOUTUBE_URL = settings.YOUTUBE_URL


class CreateOrGetVideo(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()

    def get(self, request, **kwargs):
        keyWord = request.GET.get("words")
        amount = request.GET.get("amount")
        videos = send_request_to_api(keyWord, amount)
        current_ids = []
        for video in videos:
            current_ids.append(video["id"])
            if not Video.objects.filter(videoId=video["id"]).exists():
                Video.objects.create_video(data=video)
        objects = Video.objects.filter(videoId__in=current_ids).values()
        current_ids.clear()
        return Response(objects)


class VideoDetail(generics.RetrieveAPIView):

    serializer_class = VideoSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Video, videoId=item)


class GetStartList(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.order_by('-id')[:30]


class EditVideo(generics.UpdateAPIView):

    serializer_class = VideoLikeSerializer
    queryset = Video.objects.all()


class GetFavoriteVideo(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = VideoSerializer
    queryset = Video.objects.order_by('-id').filter(isFavorite=True)


def send_request_to_api(request, amount=1):
    request.replace(" ", "%")
    request.lower()

    response = requests.get(
        f'{YOUTUBE_URL}'
        f'part=snippet&type=video&maxResults={amount}&videoType=any&q={request}&'
        f'key={YOUTUBE_KEY1}')

    dataToSave = {
        "id": None,
        "image": None,
        "title": None,
        "description": None,
        "publishTime": None,
        "channelTitle": None,
    }
    data = json.loads(response.text)
    result = []
    if len(data) > 0:
        for el in data["items"]:
            dataToSave["id"] = el["id"]["videoId"]
            dataToSave["image"] = el["snippet"]["thumbnails"]["high"]["url"]
            dataToSave["title"] = el["snippet"]["title"]
            dataToSave["publishTime"] = el["snippet"]["publishTime"]
            dataToSave["description"] = el["snippet"]["description"]
            dataToSave["channelTitle"] = el["snippet"]["channelTitle"]
            result.append(dataToSave.copy())
    else:
        print("YOUTUBE QUOTA LIMIT")
    return result


