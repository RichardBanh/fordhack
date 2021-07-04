from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from users.models import Users
from users.serializers import UsersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers, status
from django.contrib.auth.models import Group

class CustomUserCreate(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format='json'):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetUserInfo(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        try:
            username = request.user.username
            userinfo = Users.objects.filter(username = username)
            serializer= UsersSerializer(userinfo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            print(request)
            return Response(status=status.HTTP_400_BAD_REQUEST)
