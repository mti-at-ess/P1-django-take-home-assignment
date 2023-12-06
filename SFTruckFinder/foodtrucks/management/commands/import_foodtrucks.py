import csv
from django.core.management.base import BaseCommand
from foodtrucks.models import FoodTruckModel
from datetime import datetime


class Command(BaseCommand):
    help = "Import food trucks from CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs["csv_file"]

        with open(csv_file_path, "r") as file:
            reader = csv.DictReader(file)
            rows = 0
            approved_date_format = "%m/%d/%Y %I:%M:%S %p"
            received_date_format = "%Y%m%d"
            for row in reader:
                FoodTruckModel.objects.create(
                    location_id=int(row["locationid"]),
                    applicant=row["Applicant"],
                    facility_type=row["FacilityType"],
                    cnn=row["cnn"],
                    location_description=row["LocationDescription"],
                    address=row["Address"],
                    blocklot=row["blocklot"],
                    block=row["block"],
                    lot=row["lot"],
                    permit=row["permit"],
                    status=row["Status"],
                    food_items=row["FoodItems"],
                    x=row["X"] if row["X"] else None,
                    y=row["Y"] if row["Y"] else None,
                    latitude=row["Latitude"],
                    longitude=row["Longitude"],
                    schedule=row["Schedule"],
                    dayshours=row["dayshours"] if row["dayshours"] else None,
                    noi_sent=row["NOISent"],
                    approved=datetime.strptime(row["Approved"], approved_date_format)
                    if row["Approved"]
                    else None,
                    received=datetime.strptime(row["Received"], received_date_format)
                    if row["Received"]
                    else None,
                    prior_permit=row["PriorPermit"],
                    expiration_date=datetime.strptime(
                        row["ExpirationDate"], approved_date_format
                    )
                    if row["ExpirationDate"]
                    else None,
                    location=row["Location"],
                    fire_prevention_districts=row["Fire Prevention Districts"] if row["Fire Prevention Districts"] else None,
                    police_districts=row["Police Districts"]if row["Police Districts"] else None,
                    supervisor_districts=row["Supervisor Districts"]if row["Supervisor Districts"] else None,
                    zip_codes=row["Zip Codes"]if row["Zip Codes"] else None,
                    neighborhoods_old=row["Neighborhoods (old)"]if row["Neighborhoods (old)"] else None,
                )
                rows += 1

        self.stdout.write(self.style.SUCCESS(f"{rows} rows imported successfully!"))
