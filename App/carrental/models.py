from django.db import models
import uuid
from django.conf import settings
# Create your models here.

def hex_uuid():
    return uuid.uuid4().hex

class RentalModel(models.Model):
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True, primary_key=True
    )
    vehicleId = models.CharField(max_length=10, blank=False, editable=False)
    active_Rent = models.BooleanField(editable=True, default=True)
    req_date = models.DateTimeField(auto_now_add=True, editable=False)
    user_who_added = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.DO_NOTHING, related_name="user_who_added")
    rental_length_days = models.CharField(max_length=4, blank=False, editable=True)
    rental_by_phone = models.CharField(max_length=10, blank=False, editable=True)
    rental_mile_limits = models.CharField(max_length=6, blank=False, editable=True)

    def __str__(self):
        return f'vehicleId: {self.vehicleId}.',f'uuid: {self.uuid}.'