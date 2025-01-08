from django.db import models

from accounts.abstracts import TimeStampedModel, UniversalIdModel, ReferenceSlugModel
from tours.models import Tour


class Booking(TimeStampedModel, UniversalIdModel, ReferenceSlugModel):
    """
    Booking model
    Guests can book a tour
    """

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name="bookings")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    guests = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default="Pending")
    request_jeep = models.BooleanField(default=False)

    # Currency and amount
    CURRENCY_CHOICES = [
        ("KSH", "Kenyan Shilling"),
        ("EURO", "Euro"),
        ("POUND", "Pound Sterling"),
        ("DOLLAR", "US Dollar"),
    ]
    currency = models.CharField(
        max_length=10, choices=CURRENCY_CHOICES, default="POUND"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_method = models.CharField(max_length=255, blank=True, null=True)
    payment_status = models.CharField(max_length=25, default="Pending")

    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.tour.title}"

    def calculate_amount(self):
        """
        Calculate amount to be paid based on currency and number of guests
        """
        rate_mapping = {
            "KSH": self.tour.ksh,
            "EURO": self.tour.euro,
            "POUND": self.tour.pound,
            "DOLLAR": self.tour.dollar,
        }
        rate = rate_mapping.get(self.currency, 0)
        return rate * self.guests

    def save(self, *args, **kwargs):
        """
        Automatically calculate and set amount before saving
        """
        self.amount = self.calculate_amount()
        super().save(*args, **kwargs)
