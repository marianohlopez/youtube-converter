from django.db import models


class ConvertedVideo(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField()
    conversion_type = models.CharField(max_length=10)
    file_path = models.FilePathField(path="media/converted_files/", blank=True)
