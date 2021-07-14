from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from .models import FleetCommandModel
from .serializer import FordUptoDateSerializer


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
            
    def post(self, request):
        action = request.data["action"]
        vehicleId = request.data["vehicleId"]

        if action == "ADD/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId, action)
            if obj["exist"] == True:
                ok_bySuper = obj["Org_obj"]["ok_bySuper"]
                ok_byCustRep = obj["Org_obj"]["ok_byCustRep"]
                return Response("Already created, Ok recieved from Customer rep: "+ str(ok_byCustRep) + ". Ok recieved from supervisor: " + str(ok_bySuper), status=status.HTTP_400_BAD_REQUEST)
            else:
                if request.user.is_staff:
                    objEntry = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action, "active_Req":True }
                    newRequest = FleetCommandModel(**objEntry)
                    newRequest.save()
                    return Response("It works", status=status.HTTP_201_CREATED)
                elif request.user.is_admin:
                    objEntry = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action, "active_Req":True}
                    newRequest = FleetCommandModel(**objEntry)
                    newRequest.save()
                    return Response("It works", status=status.HTTP_201_CREATED)
        
        elif action == "OK/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId, action)
            print(obj)
            
            if obj["exist"] == True:
                dataObj = obj["obj"]
                if request.user.is_staff:
                    if dataObj["ok_byCustRep"]:
                        return Response("Already approved by another customer rep:" + str(dataObj["CustRep_Ok"]["username"]), status=status.HTTP_208_ALREADY_REPORTED)
                    else:
                        if dataObj["ok_byCustRep"]:
                            req = Request()
                            result = req.requestFleetCommandPost(vehicleId, "/stopEngine")
                            if result["success"]:
                                dataObj.update(ok_bySuper = True,Super_Ok = request.user,active_Req = False)
                                return Response("ENGINE IS OFF, Pending request is completed. Response from ford: " + result.request["commandStatus"], status=status.HTTP_200_OK)
                            else:
                                return Response("Ford request failed", status=status.HTTP_404_NOT_FOUND)
                            
                elif request.user.is_admin:
                    if dataObj["ok_bySuper"]:
                        return Response("Already approved by another supervisor: " + str(dataObj["Super_Ok"]["username"]), status=status.HTTP_208_ALREADY_REPORTED)
                    else:
                        dataObj.update(ok_bySuper = True, Super_Ok = request.user)
                        if dataObj.ok_bySuper:
                            req = Request()
                            result = req.requestFleetCommandPost(vehicleId, "/stopEngine")
                            if result["success"]:
                                dataObj.update(active_Req = False)
                                return Response("ENGINE IS OFF, Pending request is completed", status=status.HTTP_200_OK)
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
                        obj = self.findExistProp(vehicleId, action)
                        obj["obj"].update(active_Req = False)
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
                        obj = self.findExistProp(vehicleId, action)
                        obj["obj"].update(active_Req = False)
                        return Response(result, status=status.HTTP_200_OK)

                elif request.user.is_admin:
                    obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/lock")
                    if result["success"]:
                        obj = self.findExistProp(vehicleId, action)
                        obj["obj"].update(active_Req = False)
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
                        obj = self.findExistProp(vehicleId, action)
                        obj["obj"].update(active_Req = False)
                        return Response(result, status=status.HTTP_200_OK)

                elif request.user.is_admin:
                    obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    req = Request()
                    result = req.requestFleetCommandPost(vehicleId, "/wake")
                    if result["success"]:
                        obj = self.findExistProp(vehicleId, action)
                        obj["obj"].update(active_Req = False)
                        return Response(result, status=status.HTTP_200_OK)