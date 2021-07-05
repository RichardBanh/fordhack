from rest_framework.response import Response
from rest_framework import permissions, serializers, status
from rest_framework.views import APIView
from veh.models import CarModel
from .models import FordUptoDateModel
from veh.serializers import CarRequestSerializer
from .serializer import FordUptoDateSerializer

from request import Request

class SystemFord(APIView):
    permission_classes = [permissions.AllowAny]

    def pullVehical_List(self):
        
            req = Request()
            reqObj = req.requestFleetListGet()
            if reqObj["success"] == False:
                return Response("Request to Ford failed", status=status.HTTP_400_BAD_REQUEST)
            for vehicles in reqObj.request['vehicles']:
                obj = CarModel.objects.filter(vehicleId=vehicles["vehicleId"])
                if obj.exists() == False:
                    serializer = CarRequestSerializer(data=vehicles)
                    serializer.is_valid()
                    if serializer.is_valid():
                        serializer.save()

            FordUptoDateModel.objects.create()
            return Response( reqObj["success"], status=status.HTTP_200_OK)
    #    reqObj.request,
            


    def post(self, request):
        response = self.pullVehical_List()
        return response
    
    def get(self, request):
        latestUpdate = FordUptoDateModel.objects.latest('req_date')
        serializer = FordUptoDateSerializer(latestUpdate)
        return Response(serializer, status=status.HTTP_200_OK)

