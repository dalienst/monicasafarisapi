from django.urls import path

from tours.views import (
    TourListView,
    TourDetailView,
    TourListCreateView,
    TourUpdateDeleteView,
)

urlpatterns = [
    path("", TourListView.as_view(), name="tour-list"),
    path("<str:reference>/", TourDetailView.as_view(), name="tour-detail"),
    path("create/", TourListCreateView.as_view(), name="tour-create"),
    path("detail/<str:slug>/", TourUpdateDeleteView.as_view(), name="tour-update"),
]
