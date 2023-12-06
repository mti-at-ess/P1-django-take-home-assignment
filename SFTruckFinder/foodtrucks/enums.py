from django.db.models import TextChoices


class FoodTruckStatus(TextChoices):
    APPROVED = "APPROVED"
    REQUESTED = "REQUESTED"
    ISSUED = "ISSUED"
    SUSPEND = "SUSPEND"
    EXPIRED = "EXPIRED"
