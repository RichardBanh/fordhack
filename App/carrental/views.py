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
            return {"exist":exist, "Org_obj":dict(OrigData.data[0]), "obj":Org_obj}
        else:
            return {"exist":False}

    def post(self, request):
        try:
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
                return Response("Rental already exists, please deactivate rental, to request a new one", status=status.HTTP_208_ALREADY_REPORTED)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        try:
            vehicleId = request.data["vehicleId"]
            action = request.data["action"]
            obj = self.findExistRental(vehicleId=vehicleId)
            if obj["exist"] == False:
                return Response("Rental is not active", status=status.HTTP_400_BAD_REQUEST)
            else:
                # stuff=obj["Org_obj"]
                entry = obj["obj"]
                if action == "CHANGE/PHONE":
                    entry.update(rental_by_phone=request.data["rental_by_phone"])
                    return Response("Phone is changed", status=status.HTTP_202_ACCEPTED)
                elif action == "CHANGE/MILES":
                    entry.update(rental_mile_limits=request.data["rental_mile_limits"])
                    return Response("Rental is miles is changed", status=status.HTTP_202_ACCEPTED)
                elif action == "CHANGE/DAYS":
                    entry.update(rental_length_days=request.data["rental_length_days"])
                    return Response("Rental is date is changed", status=status.HTTP_202_ACCEPTED)
                elif action == "FINISH/RENT":
                    entry.update(active_Rent=False)
                    return Response("Rental is deactivated", status=status.HTTP_202_ACCEPTED)
                else:
                    return Response("Missing action, or data input", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request):
        try:
            rentals = RentalModel.objects.filter(active_Rent=True)
            serializer = CarRentalSerializer(rentals, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)