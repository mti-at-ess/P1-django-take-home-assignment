from rest_framework.serializers import ModelSerializer
from foodtrucks.models import FoodTruckModel


class FoodTruckSerializer(ModelSerializer):
    class Meta:
        model = FoodTruckModel
        fields = "__all__"
