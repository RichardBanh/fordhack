from veh.models import CarModel

from rest_framework.response import Response
from rest_framework import permissions, status
# Create your views here.
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http import Http404
from rest_framework.views import APIView
from serializers import CarRequestSerializer
import requests

class CarsList(APIView):

    bearer = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlMxUEZhdzdkR2s3bHNFQmEzUjVWMnRLSzVYYnNIWEJsemFXZGhjNUVNdW8ifQ.eyJpc3MiOiJodHRwczovL2RhaDJ2YjJjcHJvZC5iMmNsb2dpbi5jb20vOTE0ZDg4YjEtMzUyMy00YmY2LTliZTQtMWI5NmI0ZjZmOTE5L3YyLjAvIiwiZXhwIjoxNjI1MjAxMDMyLCJuYmYiOjE2MjUxOTk4MzIsImF1ZCI6ImMxZTRjMWEwLTI4NzgtNGU2Zi1hMzA4LTgzNmIzNDQ3NGVhOSIsImxvY2FsZSI6ImVuIiwiaWRwIjoiYjJjX0RwSzFPQW44ZFEiLCJtdG1JZCI6IjU1Y2FhZTRjLWIxZDMtNDAxMC1iZWI1LWRhMDNhNjI1MTM1NCIsInVzZXJHdWlkIjoiT3J3enNKcDVRcXlKWHNrVjRVSHpOczhPUlY2MVI1ZXR2QnlwTDduTTdTY1F2NithNHlNSjVsc3dUZC9ic0FnRCIsInN1YiI6Ijc0YjdkZjI4LWFmNzEtNDc5NS1hNGJmLWNkZTJjYjMyNDlhNCIsIm5vbmNlIjoiMTIzNDU2Iiwic2NwIjoiYWNjZXNzIiwiYXpwIjoiMzA5OTAwNjItOTYxOC00MGUxLWEyN2ItN2M2YmNiMjM2NThhIiwidmVyIjoiMS4wIiwiaWF0IjoxNjI1MTk5ODMyfQ.Gh2-VBu3c4WwznF8Xxgl6-M061fGMpLaNXoTTFbd0MLxjErsPDxS5yp-QkMm9V8H50DMiW7dfieZj8xWykfpY18CwQCdorIRl1BUC9gDs2WpEdt6piJG2sFxcJUjBD5DxoieH0Z2h8sJY-GmCT9IRFgWeciVImE8fbOEBdtOrHhESN3HDykNG3NBYnNAuhxb2e5NvDNG2nkMueOfsEtje3pshN9cD4hnukuUvuSGKBRpZdx5zc1fQSEAAEyuL9HzPu6Pe4c967XFd8sYoKndHmHgPR-86RJ8iHBTRPbRaN3dyEpmGzfY8KK07ZdyKOxhtqRq5XOdy7poX8FZtp42rA"

    appId = "afdc085b-377a-4351-b23e-5e1d35fb3700"

    def getDetail(self, vehId):
        headers={"Authorization" : "Bearer " + self.bearer,
        "Application-Id":self.appId}
        try:
            request = requests.post('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + str(vehId) + '/unlock', headers=headers).json()
            success = True
            return request, success
        except:
            success = False
            return success

    def getcar_obj_db(self, vehicleId):
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        reqTyp = request.type
        if reqTyp == "ALL":
            try:
                car = CarModel.objects.all()
                serializer = CarRequestSerializer(car, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response("Whoops something is funky with the server", status=status.HTTP_400_BAD_REQUEST)
        # elif reqTyp == "DETAIL":
        #     try:
