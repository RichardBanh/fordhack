from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from .models import FleetCommandModel



from request import Request


class FleetCommand(APIView):
    permission_classes = [permissions.AllowAny]

    def findExistProp(self, vehicleId):
        
        Org_obj = FleetCommandModel.objects.filter(vehicleId=vehicleId, active_Req=False)
        print("whoops")
        exist = True
        if Org_obj:
            exist = True
            OrgList= list(Org_obj)
            return {"exist":exist, "Org_obj":OrgList}
        else:
            return {"exist":False}
            



    def post(self, request):
        action = request.data["action"]
        vehicleId = request.data["vehicleId"]

        if action == "ADD/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId)
            if obj["exist"] == True:
                ok_bySuper = obj["Org_obj"].ok_bySuper
                ok_byCustRep = obj["Org_obj"].ok_byCustRep
                return Response("Already created, Ok recieved from Customer rep: "+ str(ok_byCustRep) + ". Ok recieved from supervisor: " + str(ok_bySuper), status=status.HTTP_400_BAD_REQUEST)
            else:
                if request.user.is_staff:
                    obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    return Response(newRequest, status=status.HTTP_201_CREATED)
                elif request.user.is_admin:
                    obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    return Response(newRequest.data, status=status.HTTP_201_CREATED)
        
        elif action == "OK/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId)
            dataObj = obj["Org_obj"]
            if obj["exist"] == True:
                if request.user.is_staff:
                    if dataObj.ok_byCustRep:
                        return Response("Already approved by another customer rep:" + str(dataObj.CustRep_Ok.username), status=status.HTTP_208_ALREADY_REPORTED)
                    else:
                        dataObj.ok_bySuper = True
                        dataObj.Super_Ok = request.user
                        dataObj.save()
                        if dataObj.ok_byCustRep:
                            req = Request()
                            result = req.requestFleetCommandPost(vehicleId, "/stopEngine")
                            if result.success:
                                dataObj.active_Req = False
                                dataObj.save()
                                return Response("ENGINE IS OFF, Pending request is completed. Response from ford: " + result.request["commandStatus"], status=status.HTTP_200_OK)
                            else:
                                return Response("Ford request failed", status=status.HTTP_404_NOT_FOUND)
                            
                elif request.user.is_admin:
                    if dataObj.ok_bySuper:
                        return Response("Already approved by another supervisor: " + str(dataObj.Super_Ok.username), status=status.HTTP_208_ALREADY_REPORTED)
                    else:
                        print("jasdfihaisdhfiuahsdiuhfiaushdfiu hit!!")
                        dataObj.ok_bySuper = True
                        dataObj.Super_Ok = request.user
                        dataObj.save()
                        if dataObj.ok_bySuper:
                            req = Request()
                            result = req.requestFleetCommandPost(vehicleId, "/stopEngine")
                            if result["success"]:
                                dataObj.active_Req = False
                                dataObj.save()
                                return Response("ENGINE IS OFF, Pending request is completed", status=status.HTTP_200_OK)
                            else:
                                return Response("Ford request failed", status=status.HTTP_404_NOT_FOUND)
            else:
                return Response("Need to create request before approval", status=status.HTTP_404_NOT_FOUND)

        elif action == "UNLOCK/VEHICLE":
            if request.user.is_staff:
                obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/unlock")
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

            
            elif request.user.is_admin:
                obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/unlock")
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

        
        elif action == "LOCK/VEHICLE":
            if request.user.is_staff:
                obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/lock")
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

            
            elif request.user.is_admin:
                obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/lock")
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

        elif action == "WAKE/VEHICLE":
            if request.user.is_staff:
                obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/wake")
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

            
            elif request.user.is_admin:
                obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                req = Request()
                result = req.requestFleetCommandPost(vehicleId, "/wake")
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)


###posible issues... unpacking data from the database and from the client may not be the same
###Model save format is not proper as in the obj format needs to be in =form



###use issues... it is searching one vehicle id what happens if there is more than one request
###need to determine if the action is completed by the car!

###need to refractor.. alot of the code repeats


##need to create two accounts... one is cust server, one is supervisor 