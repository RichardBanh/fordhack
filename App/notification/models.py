from django.db import models
import uuid

# Create your models here.
def hex_uuid():
    return uuid.uuid4().hex

class MessageNotificationModel(models.Model):
    vehicleId = models.CharField(max_length=255, blank=False, editable=False)
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True, primary_key=True
    )
    last_sent = models.DateField(auto_now_add=True, editable=True)
    messageType = models.CharField(max_length=50, blank=False, editable=False)
    web = models.BooleanField(editable=False)
    message = models.CharField(max_length=255, blank=False, editable=False)
    active_Rental = models.BooleanField(editable=True, default=True)
    text_sent = models.IntegerField()

    def __str__(self):
        return f'vehicleId: {self.vehicleId}.',f'uuid: {self.uuid}.'