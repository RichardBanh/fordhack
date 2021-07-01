import requests
from django.http import Http404
from rest_framework import response
# Create your views here.
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
import os
from veh.models import CarModel
from veh.serializers import CarRequestSerializer

class SystemFord(APIView):
    permission_classes = [permissions.AllowAny]
    bearertok = os.environ.get("FORDAPIKEY")

    def pullVehical_List(self):
        headers={ "Authorization": "Bearer "+ str(self.bearertok),
        "Application-Id":"afdc085b-377a-4351-b23e-5e1d35fb3700"}
        try:
            r = requests.get('https://api.mps.ford.com/api/fordconnect/vehicles/v1', headers=headers).json()
            for vehicles in r.vehicles:
                obj = CarModel.objects.filter(vehicleId=vehicles["vehicleId"])
                if obj.exists() == False:
                    serializer = CarRequestSerializer(data=vehicles)
                    if serializer.is_valid():
                        serializer.save()
                    else:
                        return Response("Ford sent wrong format", status=status.HTTP_400_BAD_REQUEST)
                    
            return Response(r, status=status.HTTP_200_OK)
        except:
            return Response("Request to Ford failed", status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        response = self.pullVehical_List()
        return response




    # def get(self, request):
        ##last update

#brain system thing