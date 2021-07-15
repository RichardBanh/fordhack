from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

from users.models import Users
from users.serializers import UsersSerializer
from request import Request
# Create your views here.
import threading
from time import sleep

from carrental.models import RentalModel
from  carrental.serializer import CarRentalSerializer
##kinda hacky but i am just testing this first :/

class Notification(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def count(self):
        # while True:
            ##run on active renters
            notifications = []
            Org_obj = RentalModel.objects.filter(active_Rent=True)
            if Org_obj:
                exist = True
                OrgList= list(Org_obj)
                OrigData = CarRentalSerializer(OrgList, many=True)
                for x in OrigData.data:
                    data = dict(x)
                    print(data)
                    rental_days = data['rental_length_days']
                    rental_phone = data['rental_by_phone']
                    rental_mile = data['rental_mile_limits']
                    rental_start = data['req_date']
                    vehicleId = data['vehicleId']
                # readableData = dict(OrigData.data)
                # print(readableData)

                # rental_Days = readableData['rental_length_days']
            # return {"exist":exist, "Org_obj":dict(OrigData.data[0]), "obj":Org_obj}
            # objReq = req.requestDetailGetOne(vehicleId)
            # objReq["request"]
            #mileage send to renter
            #proximity issues send to renter and owner
            #tirepressure send to renter and owner
            #out of gas send to owner
            ##calculate the distance and time limit
            ##add notifications to table
            ##send texts afterwards
            ##then send texts
            
            sleep(7200)
    
    def post(self, request):
        # threading.Thread(target=self.count).start()
        self.count()
    
    # def get(self, request):
        #get notification per vehicle


