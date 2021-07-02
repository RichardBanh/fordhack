from veh.models import CarModel

from rest_framework.response import Response
from rest_framework import permissions, status
# Create your views here.
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import Http404
from rest_framework.views import APIView
from serializers import CarRequestSerializer


class CarsList(APIView):

    def getcar_obj(self, vehicleId):
            try:
                return CarModel.objects.get(vehicleId=vehicleId)
            except ObjectDoesNotExist:
                raise Http404

    # def post(self, request):
    #     serializer = CarRequestSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        car = self.getcar_obj(uuid=request.data["vehicleId"])
        serializer = CarRequestSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            car = CarModel.objects.all()
            serializer = CarRequestSerializer(car, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response("Whoops something is funky with the server", status=status.HTTP_400_BAD_REQUEST)

            
