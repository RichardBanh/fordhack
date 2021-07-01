from rest_framework import serializers
from models import FordUptoDateModel

class FordUptoDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = FordUptoDateModel
        fields = (
            'uuid',
            'req_date'
        )