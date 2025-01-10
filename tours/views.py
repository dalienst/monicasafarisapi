from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

from tours.models import Tour
from tours.serializers import TourSerializer


class TourListView(generics.ListAPIView):
    serializer_class = TourSerializer
    permission_classes = (AllowAny,)
    queryset = Tour.objects.all()


class TourDetailView(generics.RetrieveAPIView):
    serializer_class = TourSerializer
    permission_classes = (AllowAny,)
    queryset = Tour.objects.all()
    lookup_field = "reference"

    def get_queryset(self):
        return super().get_queryset().filter(reference=self.kwargs["reference"])


class TourListCreateView(generics.ListCreateAPIView):
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    serializer_class = TourSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Tour.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class TourUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TourSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Tour.objects.all()
    lookup_field = "slug"

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
