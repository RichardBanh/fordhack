from django.shortcuts import render

import requests
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

from models import FleetCommandModel
# Create your views here.
# require owners okay... limit engine turnoff one at a time

class FleetCommand(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        action = request.data["action"]
        vehicleId = request.data["vehicleId"]
        ##Get most reci
        obj = FleetCommandModel.objects.get(vehicleId=vehicleId)
        existCondition = obj.exists()
        ##check if exists 
        ##check who is requesting
        if existCondition:
            ##serialize and modify
            if action == "turnOffEngine":
        else:
            ##create