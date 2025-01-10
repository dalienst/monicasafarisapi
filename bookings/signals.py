from django.db.models.signals import post_save
from django.dispatch import receiver

from bookings.models import Booking
from bookings.utils import send_client_booking_email, notify_owner_of_booking


@receiver(post_save, sender=Booking)
def handle_booking_notifications(sender, instance, created, **kwargs):
    """
    Signal to handle booking-related notifications.
    """
    if created:
        # Notify the client
        send_client_booking_email(instance)

        # Notify the tour owner
        notify_owner_of_booking(instance)
