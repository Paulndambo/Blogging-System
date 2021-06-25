
from django.db import models

# Create your models here.
status = (
	("Delivered", "Delivered"),
	("In Transit", "In Transit"),
	("Waiting Disburse", "Waiting Disburse"),
)

transportation = (
	("Air Transport", "Air Transport"),
	("Sea Transport", "Sea Transport"),
	("Road Transport", "Road Transport"),
)

class Shipment(models.Model):
	tracking_number = models.CharField(max_length=200, unique=True)
	send_by = models.CharField(max_length=200, null=True)
	origin_country = models.CharField(max_length=200, null=True)
	title = models.CharField(max_length=500, null=True)
	description =models.TextField(null=True)
	quantity = models.CharField(max_length=200, null=True)
	send_to = models.CharField(max_length=200, null=True)
	receiver_phone_number = models.CharField(max_length=200, null=True)
	receiver_email = models.CharField(max_length=200, null=True)
	receiver_postal_code = models.CharField(max_length=200, null=True)
	receiver_zip_code = models.CharField(max_length=200, null=True)
	receiver_city = models.CharField(max_length=200, null=True)
	receiver_country = models.CharField(max_length=200, null=True)
	receiver_pickup_station = models.CharField(max_length=200, null=True)
	shipment_status = models.CharField(max_length=20, choices=status, null=True)
	shipping_method = models.CharField(max_length=200, choices=transportation, null=True)


	def __str__(self):
		return self.tracking_number + " "+ self.title
