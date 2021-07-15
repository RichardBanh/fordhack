import re
from django.shortcuts import render
from request import Request
from rest_framework import permissions, status
from rest_framework.views import APIView
from .serializer import CarRentalSerializer
from .models import RentalModel
from rest_framework.response import Response
# Create your views here.
class Rental(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def findExistRental(self, vehicleId): 
        Org_obj = RentalModel.objects.filter(active_Rent=True,vehicleId=vehicleId)
        if Org_obj:
            exist = True
            OrgList= list(Org_obj)
            OrigData = CarRentalSerializer(OrgList, many=True)
            return {"exist":exist, "Org_obj":dict(OrigData.data[0]), "obj":Org_obj[0]}
        else:
            return {"exist":False}

    def post(self, request):
        vehicleId = request.data["vehicleId"]
        obj = self.findExistRental(vehicleId=vehicleId)
        # print(vehicleId)
        # print(obj["exist"])
        # print(obj["Org_obj"])
        if obj["exist"] == False:
            objEntry = {"vehicleId":request.data["vehicleId"], "rental_length_days":request.data["rental_length_days"],"rental_by_phone": request.data["rental_by_phone"],"rental_mile_limits":request.data["rental_mile_limits"], "user_who_added":request.user}
            rental = RentalModel(**objEntry)
            rental.save()
            return Response("Rental Added", status=status.HTTP_201_CREATED)
        else:
            return Response("Rental already exists, please deactivate current request", status=status.HTTP_208_ALREADY_REPORTED)
    
    def put(self, request):
        vehicleId = request.data["vehicleId"]
        obj = self.findExistRental(vehicleId=vehicleId)
        if obj["exist"] == False:
            return Response("Rental is not active", status=status.HTTP_400_BAD_REQUEST)
        else:
            entry = obj["obj"]
            print(entry)