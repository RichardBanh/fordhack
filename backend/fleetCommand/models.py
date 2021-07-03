from django.db import models
import uuid
from django.contrib.auth.models import User



def hex_uuid():
    return uuid.uuid4().hex

class FleetCommandModel(models.Model):
    vehicleId = models.CharField(max_length=255, blank=False, unique=True, editable=False)
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True, primary_key=True
    )
    req_date = models.DateTimeField(auto_now_add=True, editable=False)
    ok_bySuper = models.BooleanField(editable=True, default=False)
    ok_byCustRep = models.BooleanField(editable=True, default=False)
    initiated_byWho = models.OneToOneField(User, editable=False, on_delete=models.DO_NOTHING)
    Super_Ok = models.OneToOneField(User, null=True, editable=False, on_delete=models.DO_NOTHING)
    CustRep_Ok= models.OneToOneField(User, null=True, editable=False, on_delete=models.DO_NOTHING)
    active_Req = models.BooleanField(editable=True, default=True)
    req = models.CharField(max_length=255, blank=False, unique=True, editable=False)

    def __str__(self):
        return (f'vehicleId: {self.vehicleId}.',f'uuid: {self.uuid}.')