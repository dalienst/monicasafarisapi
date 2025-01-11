from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from bookings.models import Booking
from bookings.serializers import BookingSerializer


class BookingCreateView(generics.CreateAPIView):
    """
    Made by the client
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (AllowAny,)


class ClientBookingDetail(generics.RetrieveAPIView):
    """
    A client can view their own booking
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (AllowAny,)
    lookup_field = "reference"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["reference"]

    def get_queryset(self):
        return super().get_queryset().filter(reference=self.kwargs["reference"])


class BookingListView(generics.ListAPIView):
    """
    Admin sees all bookings made by clients to their tours
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["reference", "date"]

    def get_queryset(self):
        return super().get_queryset().filter(tour__user=self.request.user)


class BookingDetailView(generics.RetrieveUpdateAPIView):
    """
    Admin can update a booking
    """

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "slug"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["reference", "date"]

    def get_queryset(self):
        return super().get_queryset().filter(slug=self.kwargs["slug"])
