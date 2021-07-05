from keyquery import Key
import requests


class Request():

    appId = "afdc085b-377a-4351-b23e-5e1d35fb3700"

    def requestFleetCommandPost(self, vehId, urlEnding):
        obj = Key()
        objBear = obj.shouldUpdate()
        print(objBear["success"])
        if objBear["success"]:
            headers={"Authorization" : "Bearer " + objBear["bear"],
            "Application-Id": self.appId}
            try:
                request = requests.post('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + str(vehId) + urlEnding, headers=headers).json()
                print(request)
                success = True
                return {"request": request, "success":success}
            except:
                success = False
                return {"success":success}
        # else:
        #     success = False
        #     return {"success":success}
    
    def requestFleetListGet(self):
        obj = Key()
        objBear = obj.shouldUpdate()
        print(objBear["bear"])
        if objBear["success"]:
            headers={"Authorization" : "Bearer " + objBear["bear"],'api-version': '2020-06-01',
            "Application-Id": self.appId}
            try:
                request = requests.get('https://api.mps.ford.com/api/fordconnect/vehicles/v1', headers=headers).json()
                success = True
                print(request)
                return {"request": request, "success":success}
            except:
                success = False
                return {"success":success}
    
    def requestDetailGet(self, vehicalId):
        obj = Key()
        objBear = obj.shouldUpdate()
        if objBear.success:
            headers={"Authorization" : "Bearer " + objBear.bear,
            "Application-Id": self.appId}
            try:
                request = requests.get('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + vehicalId, headers=headers).json()
                success = True
                return {"request":request, "success":success}
            except:
                success = False
                return {"success":success}

