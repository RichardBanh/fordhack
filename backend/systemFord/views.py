import requests
from django.http import Http404
# Create your views here.
from rest_framework.response import Response
from rest_framework import permissions, status


class systemFord(APIView):

    def pullVehical_List(params):
        r = requests.get('https://api.mps.ford.com/api/fordconnect/vehicles/v1', params=request.GET)
        if r.status_code > 399:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_201_CREATED)

    def post(self, request):
        response = self.pullVehical_List()

    # def get(self, request):
        ##last update

#brain system thing