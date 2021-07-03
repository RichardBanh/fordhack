from keyquery import Key
import requests


class Request():

    appId = "afdc085b-377a-4351-b23e-5e1d35fb3700"

    def requestFleetCommandPost(self, vehId, urlEnding):
        objBear = Key.shouldUpdate()
        if objBear.success:
            headers={"Authorization" : "Bearer " + objBear.bear,
            "Application-Id": self.appId}
            try:
                request = requests.post('https://api.mps.ford.com/api/fordconnect/vehicles/v1/' + str(vehId) + urlEnding, headers=headers).json()
                success = True
                return request, success
            except:
                success = False
                return success
    
    def requestFleetListGet(self):
        objBear = Key.shouldUpdate()
        if objBear.success:
            headers={"Authorization" : "Bearer " + objBear.bear,
            "Application-Id": self.appId}
            try:
                request = requests.get('https://api.mps.ford.com/api/fordconnect/vehicles/v1/', headers=headers).json()
                success = True
                return request, success
            except:
                success = False
                return success

