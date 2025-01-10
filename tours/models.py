from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

from accounts.abstracts import UniversalIdModel, TimeStampedModel, ReferenceSlugModel

User = get_user_model()


class Tour(UniversalIdModel, TimeStampedModel, ReferenceSlugModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tours")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField("tours", blank=True, null=True)
    ksh = models.DecimalField(max_digits=10, decimal_places=2)
    euro = models.DecimalField(max_digits=10, decimal_places=2)
    pound = models.DecimalField(max_digits=10, decimal_places=2)
    dollar = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=255, blank=True, null=True)
    capacity = models.CharField(blank=True, null=True, max_length=255)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
