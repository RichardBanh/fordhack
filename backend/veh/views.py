from veh.models import CarModel
from request import Request
from serializers import CarRequestSerializer

from rest_framework.response import Response
from rest_framework import permissions, status
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

from rest_framework.views import APIView


class CarsList(APIView):

    def put(self, request):
        car = self.getcar_obj(uuid=request.data["vehicleId"])
        serializer = CarRequestSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        reqTyp = request.data["type"]
        if reqTyp == "ALL":
            try:
                car = CarModel.objects.all()
                serializer = CarRequestSerializer(car, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Whoops something is funky with the server", status=status.HTTP_400_BAD_REQUEST)
        elif reqTyp == "ONE/DETAIL":
            vehicleId = request.vehicleId
            objReq = Request.requestDetailGet(vehicleId)
            if objReq.success:
                return Response(objReq.request, status=status.HTTP_200_OK)



