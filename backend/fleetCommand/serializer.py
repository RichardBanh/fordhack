from rest_framework import serializers
from .models import FleetCommandModel

class FordUptoDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FleetCommandModel
        fields = (
            'uuid',
            'vehicleId',
            'ok_bySuper',
            'ok_byCustRep',
            'initiated_byWho',
            'Super_Ok',
            'CustRep_Ok',
            'active_Req',
            'req',
            'req_date'
        )