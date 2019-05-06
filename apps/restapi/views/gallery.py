from datetime import datetime

from rest_framework import generics, status
from rest_framework.response import Response

from apps.gallery.models import Image, Video
from apps.restapi.serializers.gallery import GalleryImageSerializer, GalleryVideoSerializer


# Gallery Image Views.

class ImageListAPIView(generics.ListAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        return Image.objects.all()


class ImageUploadAPIView(generics.CreateAPIView):
    serializer_class = GalleryImageSerializer

    def post(self, request, *args, **kwargs):
        image = Image()
        image.image = request.data.get('image')
        image.desc = request.data.get('desc')
        image.tags = request.data.get('tags')
        date_upload = datetime.now()
        image.upload_date = date_upload
        image.save()
        return Response(GalleryImageSerializer(image).data, status=status.HTTP_200_OK)


class ImageUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        return Image.objects.all()

    def patch(self, request, *args, **kwargs):
        image_id = self.kwargs['pk']
        image = Image.objects.get(id=image_id)

        if image:
            image.upload_date = datetime.now()
            if request.data.get('image') is not None:
                image.image = request.data.get('image')
            if request.data.get('desc') is not None:
                image.desc = request.data.get('desc')
            if request.data.get('tags') is not None:
                image.tags = request.data.get('tags')
                image.save()
            return Response(GalleryImageSerializer(image).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Image Not found"}, status=status.HTTP_400_BAD_REQUEST, )


class ImageDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        return Image.objects.all()

    def destroy(self, request, *args, **kwargs):
        image_id = self.kwargs['pk']
        image = Image.objects.get(id=image_id)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Gallery Video Views.
class VideoListAPIView(generics.ListAPIView):
    serializer_class = GalleryVideoSerializer

    def get_queryset(self):
        return Video.objects.all()


class VideoUploadAPIView(generics.CreateAPIView):
    serializer_class = GalleryVideoSerializer

    def post(self, request, *args, **kwargs):
        video = Video()
        video.url = request.data.get('url')
        video.desc = request.data.get('desc')
        video.tags = request.data.get('tags')
        date_upload = datetime.now()
        video.upload_date = date_upload
        video.save()
        return Response(GalleryImageSerializer(video).data, status=status.HTTP_200_OK)


class VideoUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = GalleryVideoSerializer

    def get_queryset(self):
        return Video.objects.all()

    def patch(self, request, *args, **kwargs):
        video_id = self.kwargs['pk']
        video = Video.objects.get(id=video_id)

        if video:
            video.upload_date = datetime.now()
            if request.data.get('url') is not None:
                video.url = request.data.get('url')
            if request.data.get('desc') is not None:
                video.desc = request.data.get('desc')
            if request.data.get('tags') is not None:
                video.tags = request.data.get('tags')
                video.save()
            return Response(GalleryVideoSerializer(video).data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Video Not found"}, status=status.HTTP_400_BAD_REQUEST, )


class VideoDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = GalleryVideoSerializer

    def get_queryset(self):
        return Video.objects.all()

    def destroy(self, request, *args, **kwargs):
        video_id = self.kwargs['pk']
        video = Video.objects.get(id=video_id)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
