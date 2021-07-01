import requests
from rest_framework.response import Response
from rest_framework import permissions, serializers, status
from rest_framework.views import APIView
from veh.models import CarModel
from models import FordUptoDateModel
from veh.serializers import CarRequestSerializer
from serializer import FordUptoDateSerializer

# import os
class SystemFord(APIView):
    permission_classes = [permissions.AllowAny]
    # bearertok = os.environ.get("FORDAPIKEY")

    def pullVehical_List(self):
        # headers={ "Authorization": "Bearer "+ str(self.bearertok),
        headers={"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlMxUEZhdzdkR2s3bHNFQmEzUjVWMnRLSzVYYnNIWEJsemFXZGhjNUVNdW8ifQ.eyJpc3MiOiJodHRwczovL2RhaDJ2YjJjcHJvZC5iMmNsb2dpbi5jb20vOTE0ZDg4YjEtMzUyMy00YmY2LTliZTQtMWI5NmI0ZjZmOTE5L3YyLjAvIiwiZXhwIjoxNjI1MTA4MjIxLCJuYmYiOjE2MjUxMDcwMjEsImF1ZCI6ImMxZTRjMWEwLTI4NzgtNGU2Zi1hMzA4LTgzNmIzNDQ3NGVhOSIsImxvY2FsZSI6ImVuIiwiaWRwIjoiYjJjX0RwSzFPQW44ZFEiLCJtdG1JZCI6IjJiN2YzMmMyLWFkY2ItNGY5Ni05MGYyLTVmZGE4MzYxOGM1MCIsInVzZXJHdWlkIjoiT3J3enNKcDVRcXlKWHNrVjRVSHpOczhPUlY2MVI1ZXR2QnlwTDduTTdTY1F2NithNHlNSjVsc3dUZC9ic0FnRCIsInN1YiI6Ijc0YjdkZjI4LWFmNzEtNDc5NS1hNGJmLWNkZTJjYjMyNDlhNCIsIm5vbmNlIjoiMTIzNDU2Iiwic2NwIjoiYWNjZXNzIiwiYXpwIjoiMzA5OTAwNjItOTYxOC00MGUxLWEyN2ItN2M2YmNiMjM2NThhIiwidmVyIjoiMS4wIiwiaWF0IjoxNjI1MTA3MDIxfQ.UPVxHX7wXANCmevNQ87VNk5phQ8aOMf54_AjR9P274lEAQLJrM3RN92Ui2BGwFg6ajSr7w0-kR0erVaQyiElDho7p3NkJHLpxyG6jp9bw4IiaPHZPVrIieTIo1TsModuebwYIimIbPY0rUEwoQPnMRPBJHTnKj59aGF8Xxm3ls0LuXQ3T-6I9Ku0q_ZsgEyGU1LoglcUiwe_1B8Lgvt-bZNFjkAiC2AKbFyrjCPZ_3ozSyvffREFUDT5Cf34lsICbPzn0V6d_z_gE9YN2R22e8FvmCICD09fJXSALrvpYYXniNst7OZGER_cjw4sdbDr84OknQkJK7Ap3z5eUK011Q",
        "Application-Id":"afdc085b-377a-4351-b23e-5e1d35fb3700"}
        try:
            r = requests.get('https://api.mps.ford.com/api/fordconnect/vehicles/v1', headers=headers).json()
            for vehicles in r['vehicles']:
                obj = CarModel.objects.filter(vehicleId=vehicles["vehicleId"])
                if obj.exists() == False:
                    serializer = CarRequestSerializer(data=vehicles)
                    serializer.is_valid()
                    if serializer.is_valid():
                        serializer.save()
                    # else:
                    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            FordUptoDateModel.objects.create()
            return Response(r, status=status.HTTP_200_OK)
        except:
            return Response("Request to Ford failed", status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        #two way request
        response = self.pullVehical_List()
        return response
    
    def get(self, request):
        latestUpdate = FordUptoDateModel.objects.latest('req_date')
        serializer = FordUptoDateSerializer(latestUpdate)
        return Response(serializer, status=status.HTTP_200_OK)

            




    # def get(self, request):
        ##last update
