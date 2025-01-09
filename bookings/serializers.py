from rest_framework import serializers
from django.contrib.auth import get_user_model

from bookings.models import Booking
from tours.models import Tour
from bookings.utils import send_client_booking_email

User = get_user_model()


class BookingSerializer(serializers.ModelSerializer):
    tour = serializers.SlugRelatedField(
        queryset=Tour.objects.all(), slug_field="reference"
    )
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    tour_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Booking
        fields = (
            "id",
            "tour",
            "name",
            "email",
            "phone",
            "date",
            "guests",
            "special_requests",
            "status",
            "request_jeep",
            "currency",
            "amount",
            "payment_method",
            "payment_status",
            "created_at",
            "updated_at",
            "slug",
            "reference",
            "tour_details",
        )

    def get_tour_details(self, obj):
        tour = obj.tour
        return {
            "reference": tour.reference,
            "title": tour.title,
            "description": tour.description,
            "ksh": tour.ksh,
            "euro": tour.euro,
            "pound": tour.pound,
            "dollar": tour.dollar,
        }
