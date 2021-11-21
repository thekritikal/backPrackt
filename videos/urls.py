from .views import CreateOrGetVideo, EditVideo, GetFavoriteVideo, GetStartList, VideoDetail
from django.urls import path

app_name = 'video_api'

urlpatterns = [
    path('', GetStartList.as_view(), name='startlist'),
    path('search/', CreateOrGetVideo.as_view(), name='listvideo'),
    path('liked/<str:pk>/', EditVideo.as_view(), name='likedvideo'),
    path('favorite/', GetFavoriteVideo.as_view(), name='favoritevideo'),
    path('video/<str:pk>/', VideoDetail.as_view(), name='detailvideo'),
]
