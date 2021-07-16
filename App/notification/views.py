from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

from users.models import Users
from users.serializers import UsersSerializer
from request import Request
# Create your views here.
import threading
from time import sleep
import datetime

from carrental.models import RentalModel
from  carrental.serializer import CarRentalSerializer
from .models import MessageNotificationModel
from .serializer import MessageNotificationSerializer
##kinda hacky but i am just testing this first :/
##need to add non rental notifications
from text import twillioSend

class Notification(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def count(self):
        while True:
            ##run on active renters
            notifications = []
            Org_obj = RentalModel.objects.filter(active_Rent=True)
            if Org_obj:
                OrgList= list(Org_obj)
                OrigData = CarRentalSerializer(OrgList, many=True)
                for x in OrigData.data:
                    data = dict(x)
                    rental_days = data['rental_length_days']
                    rental_phone = data['rental_by_phone']
                    rental_mile = data['rental_mile_limits']
                    rental_start = data['req_date']
                    vehicleId = data['vehicleId']
                    now = datetime.datetime.now(datetime.timezone.utc)
                    date_timeObj = datetime.datetime.strptime(rental_start, "%Y-%m-%dT%H:%M:%S.%f%z")
                    timeDiff = now - date_timeObj
                    sec = timeDiff.total_seconds()
                    days = (sec / 86400 )
                    days_left_for = float(rental_days)-days
                    if (days_left_for < 2):
                        Org_obj = MessageNotificationModel.objects.filter(vehicleId=vehicleId, messageType="RETURN",active_Rental=True)
                        if Org_obj:
                            OrgList= list(Org_obj)
                            OrigData = MessageNotificationSerializer(OrgList, many=True)
                            data = dict(OrigData.data[0])
                            lastSent = data["last_sent"]
                            date_timeObj = datetime.datetime.strptime(lastSent, "%Y-%m-%dT%H:%M:%S.%f%z")
                            timeDiff = now - date_timeObj
                            sec = timeDiff.total_seconds()
                            hours = ( sec / 3600 )
                            if ( hours > 5 ):
                                obj = {"message": "Kind reminder, Your Ford rental is due to be returned", "phone": rental_phone }
                                notifications.append(obj)
                                Org_obj.update(text_sent=F('text_sent')+ 1 )
                        else:
                            end_date = now + datetime.timedelta(days=2)
                            end_date_str = str(end_date)
                            Org_obj = MessageNotificationModel(vehicleId=vehicleId, messageType="RETURN", web=True, message=vehicleId+ " will be returned on "+ end_date_str, text_sent=1)
                            Org_obj.save()
                            obj = {"message": "Kind reminder, Your Ford rental is due to be returned", "phone": rental_phone }
                            notifications.append(obj)
                    
                    req = Request()
                    objReq = req.requestDetailGetOne(vehicleId)
                    if objReq['success']:
                        reqData = objReq['request']
                        batteryEmpty = reqData['vehicle']['vehicleDetails']['batteryChargeLevel']['distanceToEmpty']
                        milage = reqData['vehicle']['vehicleDetails']['mileage']
                        if (int(milage) > int(rental_mile)):
                            Org_obj = MessageNotificationModel.objects.filter(vehicleId=vehicleId, messageType="MILEAGEWARNING",active_Rental=True)
                            if Org_obj:
                                OrgList= list(Org_obj)
                                OrigData = MessageNotificationSerializer(OrgList, many=True)
                                data = dict(OrigData.data[0])
                                lastSent = data["last_sent"]
                                date_timeObj = datetime.datetime.strptime(lastSent, "%Y-%m-%dT%H:%M:%S.%f%z")
                                timeDiff = now - date_timeObj
                                sec = timeDiff.total_seconds()
                                hours = ( sec / 3600 )
                                if ( hours > 5 ):
                                    obj = {"message": "Kind reminder, You are exceeding your rental mileage. Call +212133322222222 to increase your milage allowance to avoid penalties", "phone": rental_phone }
                                    notifications.append(obj)
                                    Org_obj.update(text_sent=F('text_sent')+ 1 )
                                    notifications.append(obj)
                            else:
                                Org_obj = MessageNotificationModel(vehicleId=vehicleId, messageType="MILEAGEWARNING", web=True, message=vehicleId+ " milage warning", text_sent=1)
                                Org_obj.save()
                                obj = {"message": "Kind reminder, You are exceeding your rental mileage. Call +212133322222222 to increase your milage allowance to avoid penalties", "phone": rental_phone }
                                notifications.append(obj)
                            
                        if (int(batteryEmpty) < 20):
                            Org_obj = MessageNotificationModel.objects.filter(vehicleId=vehicleId, messageType="CHARGEWARNING",active_Rental=True)
                            if Org_obj:
                                OrgList= list(Org_obj)
                                OrigData = MessageNotificationSerializer(OrgList, many=True)
                                data = dict(OrigData.data[0])
                                date_timeObj = datetime.datetime.strptime(lastSent, "%Y-%m-%dT%H:%M:%S.%f%z")
                                timeDiff = now - date_timeObj
                                sec = timeDiff.total_seconds()
                                hours = ( sec / 3600 )
                                if ( hours > 5 ):
                                    obj = {"message": "Kind reminder, You are dangerously low on charge", "phone": rental_phone }
                                    Org_obj.update(text_sent=F('text_sent')+ 1 )
                                    notifications.append(obj)
                            else:
                                Org_obj = MessageNotificationModel(vehicleId=vehicleId, messageType="CHARGEWARNING", web=True, message=vehicleId+ " 20 mile charge left", text_sent=1)
                                Org_obj.save()
                                obj = {"message": "Kind reminder, You are dangerously low on charge", "phone": rental_phone }
                                notifications.append(obj)
                            
                        if (reqData['vehicle']['vehicleStatus']['tirePressureWarning']):
                            Org_obj = MessageNotificationModel.objects.filter(vehicleId=vehicleId, messageType="TIREPRESSURE",active_Rental=True)
                            if Org_obj:
                                OrgList= list(Org_obj)
                                OrigData = MessageNotificationSerializer(OrgList, many=True)
                                data = dict(OrigData.data[0])
                                date_timeObj = datetime.datetime.strptime(lastSent, "%Y-%m-%dT%H:%M:%S.%f%z")
                                timeDiff = now - date_timeObj
                                sec = timeDiff.total_seconds()
                                hours = ( sec / 3600 )
                                if ( hours > 5 ):
                                    obj = {"message": "Kind reminder, Check your tires", "phone": rental_phone }
                                    Org_obj.update(text_sent=F('text_sent')+ 1 )
                                    notifications.append(obj)
                            else:
                                Org_obj = MessageNotificationModel(vehicleId=vehicleId, messageType="TIREPRESSURE", message=vehicleId+ "tire pressure indicator", text_sent=1)
                                Org_obj.save()
                                obj = {"message": "Kind reminder, Check your tire pressure", "phone": rental_phone }
                                notifications.append(obj)
            
            for x in notifications:
                twillioSend(message=x["message"],to=x["phone"])
                sleep(10)
            sleep(7200)
    
    def put(self, request):
        try:
            threading.Thread(target=self.count).start()
            return Response("Running", status=status.HTTP_200_OK)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            Org_obj = MessageNotificationModel.objects.filter(active_Rental=True)
            if Org_obj:
                OrgList= list(Org_obj)
                OrigData = MessageNotificationSerializer(OrgList, many=True)
                return Response(OrigData.data, status=status.HTTP_200_OK)
            else:
                return Response("No notifications avaliable", status=status.HTTP_200_OK)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request):
        try:
            uuid = request.data["uuid"]
            Org_obj = MessageNotificationModel.objects.get(uuid=uuid)
            Org_obj.delete()
            return Response("DELETED", status=status.HTTP_200_OK)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            action = request.data["action"]
            vehicleId = request.data["vehicleId"]
            if action == "ONE/NOTIFICATIONS":
                Org_obj = MessageNotificationModel.objects.filter(active_Rental=True, vehicleId=vehicleId)
                if Org_obj:
                    OrgList= list(Org_obj)
                    OrigData = MessageNotificationSerializer(OrgList, many=True)
                    return Response(OrigData.data, status=status.HTTP_200_OK)
                else:
                    return Response("No notifications", status=status.HTTP_204_NO_CONTENT)
            else:
                return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("Bad request", status=status.HTTP_400_BAD_REQUEST)

#phone format needs to be '+18042774771'