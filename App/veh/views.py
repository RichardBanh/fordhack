from veh.models import CarModel
from request import Request
from .serializers import CarRequestSerializer

from rest_framework.response import Response
from rest_framework import permissions, status

from rest_framework.views import APIView


class CarsList(APIView):
    permission_classes = [permissions.IsAuthenticated]

    
    def put(self, request):
        try:
            car = self.getcar_obj(uuid=request.data["vehicleId"])
            serializer = CarRequestSerializer(car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            reqTyp = request.data["type"]
            if reqTyp == "ALL":
                try:
                    car = CarModel.objects.all()
                    serializer = CarRequestSerializer(car, many=True)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    return Response("Whoops something is funky with the server", status=status.HTTP_400_BAD_REQUEST)
            elif reqTyp == "ONE/DETAIL":
                vehicleId = request.data["vehicleId"]
                req = Request()
                objReq = req.requestDetailGetOne(vehicleId)
                if objReq["success"]:
                    return Response(objReq["request"], status=status.HTTP_200_OK)
                else:
                    return Response("Request failed", status=status.HTTP_200_OK)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)