from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from users.models import Users
from users.serializers import UsersSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers, status
from django.contrib.auth.models import Group

# @api_view(['GET'])
# def current_user(request):
#     """Redirect authenticated doctors to DoctorsDetail view"""
#     if request.user.is_staff:
#         raise PermissionDenied()
#     users_uuid = Users.objects.filter(user=request.user.pk).first().uuid
#     return redirect(reverse('doctors-detail', kwargs={'uuid': users_uuid}))

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


        

    # def delete(self, request, uuid, format=None):
    #     doctor = self.get_doctor(uuid)
    #     doctor.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


class GetUserInfo(APIView):
    # authentication_classes = [permissions.IsAuthenticated]
    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        try:
            username = request.user.username
            userinfo = Users.objects.filter(username = username)
            serializer= UsersSerializer(userinfo, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            print(request)
            return Response(status=status.HTTP_400_BAD_REQUEST)


