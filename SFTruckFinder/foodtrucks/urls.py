from django.urls import path
from .views import FoodTruckListView

urlpatterns = [
    path('fetch_trucks/', FoodTruckListView.as_view(), name='nearest-foodtrucks'),
]