from django.db import models
import uuid
from django.contrib.auth.models import User



def hex_uuid():
    return uuid.uuid4().hex

class FleetCommandModel(models.Model):
    vehicleId = models.CharField(max_length=255, blank=False, unique=True, editable=False)
    uuid = models.CharField(
        max_length=32, default=hex_uuid, editable=False, unique=True
    )
    req_date = models.DateTimeField(auto_now_add=True, editable=False)
    ok_bySuper = models.BooleanField(editable=True, default=False)
    ok_byCustRep = models.BooleanField(editable=True, default=False)
    initiated_byWho = models.OneToOneField(User, editable=False)
    Super_Ok = models.OneToOneField(User, null=True, editable=False)
    CustRep_Ok= models.OneToOneField(User, null=True, editable=False)
    active_Req = models.BooleanField(editable=True, default=True)
    
    def __str__(self):
        return self.vehicleId