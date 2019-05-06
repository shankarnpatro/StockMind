from django.contrib import admin

# Register your models here.
from apps.gallery.models import Image, Video

admin.site.register(Image)
admin.site.register(Video)
