from django.db import models

# Create your models here.
from apps.usermgmt.models import User


class Image(models.Model):
    image = models.ImageField(upload_to='images/Upload_image', blank=True, null=True)
    desc = models.TextField(blank=True, default='')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc[0:10].capitalize() + "....."

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'Images'


class Video(models.Model):
    url = models.URLField(max_length=250, default='')
    desc = models.TextField(blank=True, default='')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc[0:10].capitalize() + "....."

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
