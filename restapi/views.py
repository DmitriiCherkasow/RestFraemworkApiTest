from rest_framework import generics
from .serializers import *
from .permissions import IsAdminOrReadOnly


class PaddAPIList(generics. ListCreateAPIView):
    queryset = Pereval_add.objects.all()
    serializer_class = PerevalSerializer


class PaddAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Pereval_add.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PaddAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Pereval_add.objects.all()
    serializer_class = PerevalSerializer
    permission_classes = (IsAdminOrReadOnly,)


class PImagesAPIList(generics. ListCreateAPIView):
    queryset = Pereval_images.objects.all()
    serializer_class = ImagesSerializer


class PImagesAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Pereval_images.objects.all()
    serializer_class = ImagesSerializer
    permission_classes = (IsAdminOrReadOnly,)
