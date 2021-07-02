from django.shortcuts import render

import requests
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView

from models import FleetCommandModel
# Create your views here.
# require owners okay... limit engine turnoff one at a time

class FleetCommand(APIView):
    permission_classes = [permissions.AllowAny]

    def stopEngine(self, vehId):
        # headers={ "Authorization": "Bearer "+ str(self.bearertok),
        headers={"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlMxUEZhdzdkR2s3bHNFQmEzUjVWMnRLSzVYYnNIWEJsemFXZGhjNUVNdW8ifQ.eyJpc3MiOiJodHRwczovL2RhaDJ2YjJjcHJvZC5iMmNsb2dpbi5jb20vOTE0ZDg4YjEtMzUyMy00YmY2LTliZTQtMWI5NmI0ZjZmOTE5L3YyLjAvIiwiZXhwIjoxNjI1MTA4MjIxLCJuYmYiOjE2MjUxMDcwMjEsImF1ZCI6ImMxZTRjMWEwLTI4NzgtNGU2Zi1hMzA4LTgzNmIzNDQ3NGVhOSIsImxvY2FsZSI6ImVuIiwiaWRwIjoiYjJjX0RwSzFPQW44ZFEiLCJtdG1JZCI6IjJiN2YzMmMyLWFkY2ItNGY5Ni05MGYyLTVmZGE4MzYxOGM1MCIsInVzZXJHdWlkIjoiT3J3enNKcDVRcXlKWHNrVjRVSHpOczhPUlY2MVI1ZXR2QnlwTDduTTdTY1F2NithNHlNSjVsc3dUZC9ic0FnRCIsInN1YiI6Ijc0YjdkZjI4LWFmNzEtNDc5NS1hNGJmLWNkZTJjYjMyNDlhNCIsIm5vbmNlIjoiMTIzNDU2Iiwic2NwIjoiYWNjZXNzIiwiYXpwIjoiMzA5OTAwNjItOTYxOC00MGUxLWEyN2ItN2M2YmNiMjM2NThhIiwidmVyIjoiMS4wIiwiaWF0IjoxNjI1MTA3MDIxfQ.UPVxHX7wXANCmevNQ87VNk5phQ8aOMf54_AjR9P274lEAQLJrM3RN92Ui2BGwFg6ajSr7w0-kR0erVaQyiElDho7p3NkJHLpxyG6jp9bw4IiaPHZPVrIieTIo1TsModuebwYIimIbPY0rUEwoQPnMRPBJHTnKj59aGF8Xxm3ls0LuXQ3T-6I9Ku0q_ZsgEyGU1LoglcUiwe_1B8Lgvt-bZNFjkAiC2AKbFyrjCPZ_3ozSyvffREFUDT5Cf34lsICbPzn0V6d_z_gE9YN2R22e8FvmCICD09fJXSALrvpYYXniNst7OZGER_cjw4sdbDr84OknQkJK7Ap3z5eUK011Q",
        "Application-Id":"afdc085b-377a-4351-b23e-5e1d35fb3700"}
        try:
            request = requests.post('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + str(vehId) + '/stopEngine', headers=headers).json()
            success = True
            return request, success
        except:
            success = False
            return success
    
    def unlock(self, vehId):
        # headers={ "Authorization": "Bearer "+ str(self.bearertok),
        headers={"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlMxUEZhdzdkR2s3bHNFQmEzUjVWMnRLSzVYYnNIWEJsemFXZGhjNUVNdW8ifQ.eyJpc3MiOiJodHRwczovL2RhaDJ2YjJjcHJvZC5iMmNsb2dpbi5jb20vOTE0ZDg4YjEtMzUyMy00YmY2LTliZTQtMWI5NmI0ZjZmOTE5L3YyLjAvIiwiZXhwIjoxNjI1MTA4MjIxLCJuYmYiOjE2MjUxMDcwMjEsImF1ZCI6ImMxZTRjMWEwLTI4NzgtNGU2Zi1hMzA4LTgzNmIzNDQ3NGVhOSIsImxvY2FsZSI6ImVuIiwiaWRwIjoiYjJjX0RwSzFPQW44ZFEiLCJtdG1JZCI6IjJiN2YzMmMyLWFkY2ItNGY5Ni05MGYyLTVmZGE4MzYxOGM1MCIsInVzZXJHdWlkIjoiT3J3enNKcDVRcXlKWHNrVjRVSHpOczhPUlY2MVI1ZXR2QnlwTDduTTdTY1F2NithNHlNSjVsc3dUZC9ic0FnRCIsInN1YiI6Ijc0YjdkZjI4LWFmNzEtNDc5NS1hNGJmLWNkZTJjYjMyNDlhNCIsIm5vbmNlIjoiMTIzNDU2Iiwic2NwIjoiYWNjZXNzIiwiYXpwIjoiMzA5OTAwNjItOTYxOC00MGUxLWEyN2ItN2M2YmNiMjM2NThhIiwidmVyIjoiMS4wIiwiaWF0IjoxNjI1MTA3MDIxfQ.UPVxHX7wXANCmevNQ87VNk5phQ8aOMf54_AjR9P274lEAQLJrM3RN92Ui2BGwFg6ajSr7w0-kR0erVaQyiElDho7p3NkJHLpxyG6jp9bw4IiaPHZPVrIieTIo1TsModuebwYIimIbPY0rUEwoQPnMRPBJHTnKj59aGF8Xxm3ls0LuXQ3T-6I9Ku0q_ZsgEyGU1LoglcUiwe_1B8Lgvt-bZNFjkAiC2AKbFyrjCPZ_3ozSyvffREFUDT5Cf34lsICbPzn0V6d_z_gE9YN2R22e8FvmCICD09fJXSALrvpYYXniNst7OZGER_cjw4sdbDr84OknQkJK7Ap3z5eUK011Q",
        "Application-Id":"afdc085b-377a-4351-b23e-5e1d35fb3700"}
        try:
            request = requests.post('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + str(vehId) + '/unlock', headers=headers).json()
            success = True
            return request, success
        except:
            success = False
            return success
    
    def lock(self, vehId):
        # headers={ "Authorization": "Bearer "+ str(self.bearertok),
        headers={"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlMxUEZhdzdkR2s3bHNFQmEzUjVWMnRLSzVYYnNIWEJsemFXZGhjNUVNdW8ifQ.eyJpc3MiOiJodHRwczovL2RhaDJ2YjJjcHJvZC5iMmNsb2dpbi5jb20vOTE0ZDg4YjEtMzUyMy00YmY2LTliZTQtMWI5NmI0ZjZmOTE5L3YyLjAvIiwiZXhwIjoxNjI1MTA4MjIxLCJuYmYiOjE2MjUxMDcwMjEsImF1ZCI6ImMxZTRjMWEwLTI4NzgtNGU2Zi1hMzA4LTgzNmIzNDQ3NGVhOSIsImxvY2FsZSI6ImVuIiwiaWRwIjoiYjJjX0RwSzFPQW44ZFEiLCJtdG1JZCI6IjJiN2YzMmMyLWFkY2ItNGY5Ni05MGYyLTVmZGE4MzYxOGM1MCIsInVzZXJHdWlkIjoiT3J3enNKcDVRcXlKWHNrVjRVSHpOczhPUlY2MVI1ZXR2QnlwTDduTTdTY1F2NithNHlNSjVsc3dUZC9ic0FnRCIsInN1YiI6Ijc0YjdkZjI4LWFmNzEtNDc5NS1hNGJmLWNkZTJjYjMyNDlhNCIsIm5vbmNlIjoiMTIzNDU2Iiwic2NwIjoiYWNjZXNzIiwiYXpwIjoiMzA5OTAwNjItOTYxOC00MGUxLWEyN2ItN2M2YmNiMjM2NThhIiwidmVyIjoiMS4wIiwiaWF0IjoxNjI1MTA3MDIxfQ.UPVxHX7wXANCmevNQ87VNk5phQ8aOMf54_AjR9P274lEAQLJrM3RN92Ui2BGwFg6ajSr7w0-kR0erVaQyiElDho7p3NkJHLpxyG6jp9bw4IiaPHZPVrIieTIo1TsModuebwYIimIbPY0rUEwoQPnMRPBJHTnKj59aGF8Xxm3ls0LuXQ3T-6I9Ku0q_ZsgEyGU1LoglcUiwe_1B8Lgvt-bZNFjkAiC2AKbFyrjCPZ_3ozSyvffREFUDT5Cf34lsICbPzn0V6d_z_gE9YN2R22e8FvmCICD09fJXSALrvpYYXniNst7OZGER_cjw4sdbDr84OknQkJK7Ap3z5eUK011Q",
        "Application-Id":"afdc085b-377a-4351-b23e-5e1d35fb3700"}
        try:
            request = requests.post('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + str(vehId) + '/lock', headers=headers).json()
            success = True
            return request, success
        except:
            success = False
            return success
    
    def wake(self, vehId):
        # headers={ "Authorization": "Bearer "+ str(self.bearertok),
        headers={"Authorization" : "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IlMxUEZhdzdkR2s3bHNFQmEzUjVWMnRLSzVYYnNIWEJsemFXZGhjNUVNdW8ifQ.eyJpc3MiOiJodHRwczovL2RhaDJ2YjJjcHJvZC5iMmNsb2dpbi5jb20vOTE0ZDg4YjEtMzUyMy00YmY2LTliZTQtMWI5NmI0ZjZmOTE5L3YyLjAvIiwiZXhwIjoxNjI1MTA4MjIxLCJuYmYiOjE2MjUxMDcwMjEsImF1ZCI6ImMxZTRjMWEwLTI4NzgtNGU2Zi1hMzA4LTgzNmIzNDQ3NGVhOSIsImxvY2FsZSI6ImVuIiwiaWRwIjoiYjJjX0RwSzFPQW44ZFEiLCJtdG1JZCI6IjJiN2YzMmMyLWFkY2ItNGY5Ni05MGYyLTVmZGE4MzYxOGM1MCIsInVzZXJHdWlkIjoiT3J3enNKcDVRcXlKWHNrVjRVSHpOczhPUlY2MVI1ZXR2QnlwTDduTTdTY1F2NithNHlNSjVsc3dUZC9ic0FnRCIsInN1YiI6Ijc0YjdkZjI4LWFmNzEtNDc5NS1hNGJmLWNkZTJjYjMyNDlhNCIsIm5vbmNlIjoiMTIzNDU2Iiwic2NwIjoiYWNjZXNzIiwiYXpwIjoiMzA5OTAwNjItOTYxOC00MGUxLWEyN2ItN2M2YmNiMjM2NThhIiwidmVyIjoiMS4wIiwiaWF0IjoxNjI1MTA3MDIxfQ.UPVxHX7wXANCmevNQ87VNk5phQ8aOMf54_AjR9P274lEAQLJrM3RN92Ui2BGwFg6ajSr7w0-kR0erVaQyiElDho7p3NkJHLpxyG6jp9bw4IiaPHZPVrIieTIo1TsModuebwYIimIbPY0rUEwoQPnMRPBJHTnKj59aGF8Xxm3ls0LuXQ3T-6I9Ku0q_ZsgEyGU1LoglcUiwe_1B8Lgvt-bZNFjkAiC2AKbFyrjCPZ_3ozSyvffREFUDT5Cf34lsICbPzn0V6d_z_gE9YN2R22e8FvmCICD09fJXSALrvpYYXniNst7OZGER_cjw4sdbDr84OknQkJK7Ap3z5eUK011Q",
        "Application-Id":"afdc085b-377a-4351-b23e-5e1d35fb3700"}
        try:
            request = requests.post('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + str(vehId) + '/wake', headers=headers).json()
            success = True
            return request, success
        except:
            success = False
            return success

    def findExistProp(self, vehicleId):
        Org_obj = FleetCommandModel.objects.get(vehicleId=vehicleId)
        exist = Org_obj.exists()
        return exist, Org_obj


    def post(self, request):
        action = request.data["action"]
        vehicleId = request.data["vehicleId"]

        if action == "ADD/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId)
            if obj.exist == True:
                ok_bySuper = obj.Org_obj.ok_bySuper
                ok_byCustRep = obj.Org_obj.ok_byCustRep
                return Response("Already created, Ok recieved from Customer rep "+ str(ok_byCustRep) + " Ok recieved from supervisor " + str(ok_bySuper), status=status.HTTP_400_BAD_REQUEST)
            else:
                if request.user.is_staff:
                    obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    return Response(newRequest.data, status=status.HTTP_201_CREATED)
                elif request.user.is_admin:
                    obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                    newRequest = FleetCommandModel(**obj)
                    newRequest.save()
                    return Response(newRequest.data, status=status.HTTP_201_CREATED)
        
        elif action == "OK/VEHICLE/SHUTTOFF/PROP":
            obj = self.findExistProp(vehicleId)
            dataObj = obj.Org_obj
            if obj.exist == True:
                if request.user.is_staff:
                    if dataObj.ok_byCustRep:
                        Response("Already approved by another customer rep:" + str(dataObj.CustRep_Ok.username), status=status.HTTP_404_NOT_FOUND)
                    else:
                        dataObj.ok_byCustRep = True
                        dataObj.CustRep_Ok = request.user
                        dataObj.save()
                        if dataObj.ok_bySuper:
                            result = self.stopEngine(vehicleId)
                            if result.success:
                                dataObj.active_Req = False
                                dataObj.save()
                                Response("ENGINE IS OFF, Pending request is completed", status=status.HTTP_200_OK)
                            else:
                                Response("Ford request failed", status=status.HTTP_404_NOT_FOUND)
                            
                elif request.user.is_admin:
                    if dataObj.ok_bySuper:
                        Response("Already approved by another customer rep:" + str(dataObj.Super_Ok.username), status=status.HTTP_404_NOT_FOUND)
            else:
                Response("Need to create request before approval", status=status.HTTP_404_NOT_FOUND)

        elif action == "UNLOCK/VEHICLE":
            if request.user.is_staff:
                obj = {"vehicleId":vehicleId, "ok_byCustRep":True, "CustRep_Ok":request.user, "initiated_byWho":request.user, "req": action }
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                result = self.unlock(vehicleId)
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

            
            elif request.user.is_admin:
                obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                result = self.unlock(vehicleId)
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
                result = self.lock(vehicleId)
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

            
            elif request.user.is_admin:
                obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                result = self.lock(vehicleId)
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
                result = self.wake(vehicleId)
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)

            
            elif request.user.is_admin:
                obj = {"vehicleId":vehicleId, "ok_bySuper":True, "Super_Ok":request.user, "initiated_byWho":request.user, "req": action}
                newRequest = FleetCommandModel(**obj)
                newRequest.save()
                result = self.wake(vehicleId)
                if result.success:
                    obj = self.findExistProp(vehicleId)
                    obj.Org_obj.active_Req = False
                    obj.save()
                    return Response("Unlocked!", status=status.HTTP_200_OK)


###posible issues... unpacking data from the database and from the client may not be the same
###Model save format is not proper as in the obj format needs to be in =form



### use issues... it is searching one vehicle id what happens if there is more than one request
### need to determine if the action is completed by the car!

### need to refractor.. alot of the code repeats