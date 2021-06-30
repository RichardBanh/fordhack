from rest_framework import serializers

from veh.models import CarModel

class CarRequestSerializer(serializers.ModelSerializer):

    class Meta: 
        model =  CarModel
        fields = (
            'vehicleId', 
            'make', 
            'model_name', 
            'model_year', 
            'color', 
            'nick_name', 
            'modem_enabled', 
            'vehicleAuthorizationIndicator', 
            'serviceCompatible',
            'registration_date'
        )
        