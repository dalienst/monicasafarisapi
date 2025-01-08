from rest_framework import serializers
from django.contrib.auth import get_user_model

from bookings.models import Booking
from tours.models import Tour

User = get_user_model()


class BookingSerializer(serializers.ModelSerializer):
    tours = serializers.SlugRelatedField(
        queryset=Tour.objects.all(), slug_field="reference"
    )
