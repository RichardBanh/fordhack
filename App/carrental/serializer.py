from rest_framework import serializers
from .models import RentalModel

class CarRentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentalModel
        fields = (
            'uuid',
            'vehicleId',
            'active_Rent',
            'user_who_added',
            'rental_length_days',
            'rental_by_phone',
            'rental_mile_limits',
            'req_date'
        )