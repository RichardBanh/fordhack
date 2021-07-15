from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

from users.models import Users
from users.serializers import UsersSerializer
from request import Request
# Create your views here.
import threading
from time import sleep

##kinda hacky but i am just testing this first :/
class Notification(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def count(self):
        while True:
            ##run on active renters
            # Org_obj = RentalModel.objects.filter(active_Rent=True,vehicleId=vehicleId)
            # if Org_obj:
            # exist = True
            # OrgList= list(Org_obj)
            # OrigData = CarRentalSerializer(OrgList, many=True)
            # readable = dict(OrigData.data[0])
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
        threading.Thread(target=self.count).start()


