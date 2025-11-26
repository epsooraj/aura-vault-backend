from django.db import models


class Photo(models.Model):
    """
    Photo model storing metadata in the database and the file itself in S3.

    The ImageField will use the DEFAULT_FILE_STORAGE defined in settings
    (S3 via django-storages), so uploaded files go directly to your S3 bucket.
    """

    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="photos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title or f"Photo {self.pk}"
