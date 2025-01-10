from django.urls import path

from tours.views import (
    TourListView,
    TourDetailView,
    TourListCreateView,
    TourUpdateDeleteView,
)

urlpatterns = [
    path("list/", TourListView.as_view(), name="tour-list"),
    path("detail/<str:reference>/", TourDetailView.as_view(), name="tour-detail"),
    path("", TourListCreateView.as_view(), name="tour-list-create"),
    path("<str:slug>/", TourUpdateDeleteView.as_view(), name="tour-update"),
]
