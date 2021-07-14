from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from .models import FleetCommandModel
from .serializer import FordUptoDateSerializer
from users.models import Users
from users.serializers import UsersSerializer

from request import Request


class FleetCommand(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def findExistProp(self, vehicleId, action): 
        Org_obj = FleetCommandModel.objects.filter(active_Req=True).filter(vehicleId=vehicleId).filter(req=action)
        if Org_obj:
            exist = True
            OrgList= list(Org_obj)
            OrigData = FordUptoDateSerializer(OrgList,many=True)
            return {"exist":exist, "Org_obj":dict(OrigData.data[0]), "obj":Org_obj}
        else:
            return {"exist":False}
    
    def getOneCommand(self, uuid):
        Org_obj = FleetCommandModel.objects.get(uuid=uuid)
        return Org_obj
            
    def post(self, request):
        action = request.data["action"]
        vehicleId = request.data["vehicleId"]
        print(request.user.is_staff, "staff")
        print(request.user.is_admin, "admin")
        if action == "ADD/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId, action)
            if obj["exist"] == True:
                ok_bySuper = obj["Org_obj"]["ok_bySuper"]
                ok_byCustRep = obj["Org_obj"]["ok_byCustRep"]
                return Response("Already created, Ok recieved from Customer rep: "+ str(ok_byCustRep) + ". Ok recieved from supervisor: " + str(ok_bySuper), status=status.HTTP_208_ALREADY_REPORTED)
            else:
                if request.user.is_staff:
                    objEntry = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action, "active_Req":True }
                    newRequest = FleetCommandModel(**objEntry)
                    newRequest.save()
                    return Response("Created by staff, Need approval from admin", status=status.HTTP_201_CREATED)
                elif request.user.is_admin:
                    objEntry = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action, "active_Req":True}
                    newRequest = FleetCommandModel(**objEntry)
                    newRequest.save()
                    return Response("Created by admin, Need approval from staff", status=status.HTTP_201_CREATED)
        
        elif action == "OK/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId, "ADD/VEHICLE/SHUTTOFF/PROP")
            if obj["exist"] == True:
                dataObj = obj["Org_obj"]
                if request.user.is_staff:
                    if dataObj["ok_byCustRep"]:
                        user = Users.objects.get(id=dataObj["CustRep_Ok"])
                        userinfo = UsersSerializer(user).data
                        return Response("Already approved by another customer rep:" + userinfo["username"], status=status.HTTP_208_ALREADY_REPORTED)
                    else:
                        if dataObj["ok_bySuper"]:
                            req = Request()
                            result = req.requestFleetCommandPost(vehicleId, "/stopEngine")
                            if result["success"]:
                                obj_to_be_updated = FleetCommandModel.objects.get(uuid=dataObj["uuid"])
                                obj_to_be_updated.ok_byCustRep = True
                                obj_to_be_updated.CustRep_Ok = request.user
                                obj_to_be_updated.active_Req = False
                                obj_to_be_updated.save()
                                return Response("ENGINE IS OFF, Pending request is completed. Response from ford: "+ result["request"]["commandStatus"], status=status.HTTP_200_OK)
                            else:
                                return Response("Ford request failed", status=status.HTTP_404_NOT_FOUND)
                            
                elif request.user.is_admin:
                
                    if dataObj["ok_bySuper"]:
                        user = Users.objects.get(id=dataObj["Super_Ok"])
                        userinfo = UsersSerializer(user).data
                        return Response("Already approved by another supervisor: " + userinfo["username"], status=status.HTTP_208_ALREADY_REPORTED)
                    else:
                        req = Request()
                        result = req.requestFleetCommandPost(vehicleId, "/stopEngine")
                        if result["success"]:
                            obj_to_be_updated = self.getOneCommand(uuid=dataObj["uuid"])
                            obj_to_be_updated.ok_bySuper = True
                            obj_to_be_updated.Super_Ok = request.user
                            obj_to_be_updated.active_Req = False
                            obj_to_be_updated.save()
                            return Response("ENGINE IS OFF, Pending request is completed. Response from ford: "+ result["request"]["commandStatus"], status=status.HTTP_200_OK)
                        else:
                            return Response("Ford request failed", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("Need to create request before approval", status=status.HTTP_404_NOT_FOUND)

        elif action == "UNLOCK/VEHICLE":
            obj = self.findExistProp(vehicleId, action)
            if obj["exist"]:
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/unlock")
                obj["obj"].update(active_Req = False)
                return Response(result, status=status.HTTP_200_OK)
            else:
                if request.user.is_staff:
                    obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/unlock")
                    # print(result)
                    if result["success"]:
                        obj = FleetCommandModel.objects.get(vehicleId=vehicleId, active_Req=True,req=action )
                        obj.active_Req=False
                        obj.save()
                        return Response(result, status=status.HTTP_200_OK)

                elif request.user.is_admin:
                    obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/unlock")
                    print(result)
                    if result["success"]:
                        obj = FleetCommandModel.objects.get(vehicleId=vehicleId, active_Req=True,req=action )
                        obj.active_Req=False
                        obj.save()
                        return Response(result, status=status.HTTP_200_OK)

        elif action == "LOCK/VEHICLE":
            obj = self.findExistProp(vehicleId, action)
            if obj["exist"]:
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/lock")
                obj["obj"].update(active_Req = False)
                return Response(result, status=status.HTTP_200_OK)
            else:
                if request.user.is_staff:
                    obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/lock")
                    if result["success"]:
                        obj = FleetCommandModel.objects.get(vehicleId=vehicleId, active_Req=True,req=action )
                        obj.active_Req=False
                        obj.save()
                        return Response(result, status=status.HTTP_200_OK)

                elif request.user.is_admin:
                    obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/lock")
                    if result["success"]:
                        obj = FleetCommandModel.objects.get(vehicleId=vehicleId, active_Req=True,req=action )
                        obj.active_Req=False
                        obj.save()
                        return Response(result, status=status.HTTP_200_OK)

        elif action == "WAKE/VEHICLE":
            obj = self.findExistProp(vehicleId, action)
            if obj["exist"]:
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/wake")
                obj["obj"].update(active_Req = False)
                return Response(result, status=status.HTTP_200_OK)
            else:
                if request.user.is_staff:
                    obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/wake")
                    if result["success"]:
                        obj = FleetCommandModel.objects.get(vehicleId=vehicleId, active_Req=True,req=action )
                        obj.active_Req=False
                        obj.save()
                        return Response(result, status=status.HTTP_200_OK)

                elif request.user.is_admin:
                    obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/wake")
                    if result["success"]:
                        obj = FleetCommandModel.objects.get(vehicleId=vehicleId, active_Req=True,req=action )
                        obj.active_Req=False
                        obj.save()
                        return Response(result, status=status.HTTP_200_OK)