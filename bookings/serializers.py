from rest_framework import serializers
from django.contrib.auth import get_user_model

from bookings.models import Booking
from tours.models import Tour

User = get_user_model()


class BookingSerializer(serializers.ModelSerializer):
    tour = serializers.SlugRelatedField(
        queryset=Tour.objects.all(), slug_field="reference"
    )
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

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
        )
