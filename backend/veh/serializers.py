from rest_framework import serializers
from veh.models import CarModel


class CarRequestSerializer(serializers.ModelSerializer):

    class Meta: 
        model =  CarModel
        fields = (
            'vehicleId', 
            'make', 
            'modelName', 
            'modelYear', 
            'color', 
            'nickName', 
            'modemEnabled', 
            'vehicleAuthorizationIndicator', 
            'serviceCompatible',
            'registration_date'
        )
        