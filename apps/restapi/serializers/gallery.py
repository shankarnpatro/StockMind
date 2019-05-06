from rest_framework import serializers

from apps.gallery.models import Image, Video


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class GalleryVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
