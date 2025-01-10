from rest_framework import serializers
from django.contrib.auth import get_user_model

from tours.models import Tour
from bookings.serializers import BookingSerializer

User = get_user_model()


class TourSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.email", read_only=True)
    image = serializers.ImageField(required=False, use_url=True)
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = (
            "id",
            "user",
            "title",
            "description",
            "image",
            "ksh",
            "euro",
            "pound",
            "dollar",
            "duration",
            "capacity",
            "is_featured",
            "bookings",
            "created_at",
            "updated_at",
            "slug",
            "reference",
        )
