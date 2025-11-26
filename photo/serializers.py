from rest_framework import serializers

from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "title", "image", "uploaded_at"]
        read_only_fields = ["id", "uploaded_at"]


