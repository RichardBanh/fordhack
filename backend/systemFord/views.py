import requests
from django.http import Http404
# Create your views here.
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
import os

class SystemFord(APIView):
    permission_classes = [permissions.AllowAny]
    bearertok = os.environ.get("FORDAPIKEY")

    def pullVehical_List(self):
        headers={ "Authorization": "Bearer "+ str(self.bearertok),
        "Application-Id":"afdc085b-377a-4351-b23e-5e1d35fb3700"}
        r = requests.get('https://api.mps.ford.com/api/fordconnect/vehicles/v1', headers=headers)
        print(r.json())
        if r.status_code > 399:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:

            print(r)
            return Response(status=status.HTTP_200_OK)

    def post(self, request):
        response = self.pullVehical_List()
        return Response(status=status.HTTP_200_OK)

    # def get(self, request):
        ##last update

#brain system thing