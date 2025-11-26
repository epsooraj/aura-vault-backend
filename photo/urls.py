from django.urls import path

from .views import PhotoListCreateAPIView

app_name = "photo"

urlpatterns = [
    # List and upload photos via REST API
    path("", PhotoListCreateAPIView.as_view(), name="photo-list-create"),
]


