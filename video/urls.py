
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('videos.urls', namespace='videos')),
    path('', include_docs_urls(title='VideoAPI')),
    path('schema', get_schema_view(
        title="VideoAPI",
        description="API for the VideoAPI",
        version="1.0.0"
    ), name='openapi-schema'),
]
