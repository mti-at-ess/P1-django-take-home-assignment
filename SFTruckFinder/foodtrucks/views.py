from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from foodtrucks.models import FoodTruckModel
from foodtrucks.serializers import FoodTruckSerializer
from foodtrucks.utils import haversine_distance
from django.core.exceptions import BadRequest


class FoodTruckListView(ListCreateAPIView):
    queryset = FoodTruckModel.objects.all()
    serializer_class = FoodTruckSerializer

    def get_queryset(self):
        longitude = float(self.request.query_params.get("latitude", None))
        latitude = float(self.request.query_params.get("longitude", None))

        if not latitude:
            raise BadRequest("Latitude value is not valid")
        if not longitude:
            raise BadRequest("Longitude value is not valid")

        queryset = FoodTruckModel.objects.filter(approved__isnull=False).exclude(longitude=0.0)

        # Filter and sort by distance using the Haversine formula
        queryset = sorted(
            queryset,
            key=lambda truck: haversine_distance(
                truck.id, latitude, longitude, truck.latitude, truck.longitude
            ),
        )

        return queryset[:5]
