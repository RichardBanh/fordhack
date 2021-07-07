from django.shortcuts import render
from rest_framework.views import APIView
from veh.models import CarModel
from veh.serializers import CarRequestSerializer
from request import Request
from rest_framework.response import Response

from rest_framework import status
# Create your views here.
class CarLocation(APIView):

    def get(self, request):
        reqType = request.data["type"]
        if reqType == "GET/ALL/LOCATIONS":
            car = CarModel.objects.all()
            serializer = CarRequestSerializer(car, many=True)
            arrayData = serializer.data
            location = []
            for obj in arrayData:
                regDic = dict(obj)
                vehicleId = regDic["vehicleId"]
                try:
                    req = Request()
                    obj = req.requestAllVehicleLocationGet(vehicleId)
                    if obj["success"]:
                        pushData = {"vehicleId":vehicleId, "vehicleLocation":obj["request"]["vehicleLocation"]}
                        location.append(pushData)
                    else:
                        error = "Something wrong with ford request format"
                        return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except:
                    error = "Something wrong with ford request"
                    return Response(error, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            return Response(location, status=status.HTTP_200_OK)