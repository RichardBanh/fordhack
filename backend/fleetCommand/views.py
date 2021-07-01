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
        ##check exist is expensive
        ##send notification that car is being actioned 
        ##ok by assignee
        # if action == "ADD/VEHICLE/SHUTTOFF/PROP":
        #     ##serialize and modify
        # elif action == "OK/VEHICLE/SHUTTOFF/PROP":
        #     ##create
        # elif action == "UNLOCK/VEHICLE":
        
        # elif action == "LOCK/VEHICLE":

        # elif action == "WAKE/VEHICLE":