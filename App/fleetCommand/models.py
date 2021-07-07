from django.db import models
import uuid
from django.conf import settings

def hex_uuid():
    return uuid.uuid4().hex

class FleetCommandModel(models.Model):
    vehicleId = models.CharField(max_length=255, blank=False, editable=False)
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True, primary_key=True
    )
    req_date = models.DateTimeField(auto_now_add=True, editable=False)
    ok_bySuper = models.BooleanField(editable=True, default=False)
    ok_byCustRep = models.BooleanField(editable=True, default=False)
    initiated_byWho = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False, on_delete=models.DO_NOTHING, related_name="initiated_byWho")
    Super_Ok = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=False, on_delete=models.DO_NOTHING, related_name="Super_Ok")
    CustRep_Ok= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, editable=False, on_delete=models.DO_NOTHING, related_name="CustRep_Ok")
    active_Req = models.BooleanField(editable=True, default=True)
    req = models.CharField(max_length=255, blank=False, editable=False)

    def __str__(self):
        return f'vehicleId: {self.vehicleId}.',f'uuid: {self.uuid}.'