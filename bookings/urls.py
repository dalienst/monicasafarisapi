from django.urls import path

from bookings.views import (
    BookingCreateView,
    ClientBookingDetail,
    BookingListView,
    BookingDetailView,
)

urlpatterns = [
    path("create/", BookingCreateView.as_view(), name="booking-create"),
    path("", BookingListView.as_view(), name="booking-list"),
    path(
        "detail/<str:reference>/", ClientBookingDetail.as_view(), name="booking-detail"
    ),
    path("<str:slug>/", BookingDetailView.as_view(), name="booking-update"),
]
