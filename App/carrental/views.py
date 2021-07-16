from rest_framework import permissions, status
from rest_framework.views import APIView
from .serializer import CarRentalSerializer
from .models import RentalModel
from rest_framework.response import Response
from text import twillioSend
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
        print(request)
        try:
            vehicleId = request.data["vehicleId"]
            obj = self.findExistRental(vehicleId=vehicleId)
            if obj["exist"] == False:
                objEntry = {"vehicleId":request.data["vehicleId"], "rental_length_days":request.data["rental_length_days"],"rental_by_phone": request.data["rental_by_phone"],"rental_mile_limits":request.data["rental_mile_limits"], "user_who_added":request.user}
                rental = RentalModel(**objEntry)
                rental.save()
                twillioSend("Thanks for borrowing a car! You will get notifications here!", request.data["rental_by_phone"])
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
                phone=obj["Org_obj"]["rental_by_phone"]
                entry = obj["obj"]
                
                if action == "CHANGE/PHONE":
                    entry.update(rental_by_phone=request.data["rental_by_phone"])
                    return Response("Phone is changed", status=status.HTTP_202_ACCEPTED)
                elif action == "CHANGE/MILES":
                    entry.update(rental_mile_limits=request.data["rental_mile_limits"])
                    return Response("Rental is miles is changed", status=status.HTTP_202_ACCEPTED)
                elif action == "CHANGE/DAYS":
                    entry.update(rental_length_days=request.data["rental_length_days"])
                    twillioSend("Time extended!", phone)
                    return Response("Rental is date is changed", status=status.HTTP_202_ACCEPTED)
                elif action == "FINISH/RENT":
                    entry.update(active_Rent=False)
                    twillioSend("Thanks for for returning your car!", phone)
                    return Response("Rental is deactivated", status=status.HTTP_202_ACCEPTED)
                else:
                    return Response("Missing action, or data input", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, vehicleD):
        try:
            print(vehicleD)
            if vehicleD == 'all':
                rentals = RentalModel.objects.filter(active_Rent=True)
                serializer = CarRentalSerializer(rentals, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                try :
                    rentals = RentalModel.objects.get(active_Rent=True, vehicleId=vehicleD )
                    serializer = CarRentalSerializer(rentals)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except rentals.DoesNotExist: 
                    return Response({"active_Rent": False}, status=status.HTTP_200_OK)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)