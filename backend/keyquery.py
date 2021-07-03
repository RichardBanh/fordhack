from systemFordK.models import accessKey
import datetime
import requests
import os


#will return message or bearer token

class Key:

    payload={'grant_type': 'refresh_token',
    'refresh_token': os.environ["FORDAPIKEY"],
    'client_id': '30990062-9618-40e1-a27b-7c6bcb23658a',
    'client_secret': 'T_Wk41dx2U9v22R5sQD4Z_E1u-l2B-jXHE'}
    headers={}

    def __accessKeyReq(self):
        try:
            request = requests.post("https://dah2vb2cprod.b2clogin.com/914d88b1-3523-4bf6-9be4-1b96b4f6f919/oauth2/v2.0/token?p=B2C_1A_signup_signin_common", headers=self.headers, data=self.payload).json()
            success = True
            bearer = request["access_token"]
            return bearer, success
        except:
            success = False
            error = "Something wrong with the refresh token"
            return success, error
    
    def __setBearer(self, token):
        bearer = token
        try:
            bearerDBobj = accessKey(access=bearer)
            bearerDBobj.save()
            success = True
            return success
        except:
            success = False
            message = "Couldnt Save new key"
            return success, message

    def __checkAccessKey():
        obj = accessKey.objects.latest('pk')
        exist = obj.exists()
        return obj, exist

    def shouldUpdate(self):
        objCheck = self.__checkAccessKey()
        bearer = objCheck.obj.access
        if objCheck.exist:
            timeOrigin = objCheck.obj.timeCreated
            t2 = datetime.datetime.now()
            timeDiff = t2 - timeOrigin
            minutes = timeDiff.total_seconds() / 60 
            if minutes >= 20:
                keyObj = self.__accessKeyReq()
                if keyObj.success:
                    bearObjSet = self.__setBearer(keyObj.bearer)
                    if bearObjSet.success:
                        bear = keyObj.bearer
                        success = bearObjSet.success
                        return bear, success
                    else:
                        message = bearObjSet.message
                        success = bearObjSet.success
                        return message, success
                else:
                    success = keyObj.success
                    message = keyObj.error
                    return success, message
            else:
                bear = bearer
                success = objCheck.exist
                return bear, success
        else:
            keyObj = self.__accessKeyReq()
            if keyObj.success:
                bearObjSet = self.__setBearer(keyObj.bearer)
                if bearObjSet.success:
                    bear = keyObj.bearer
                    success = bearObjSet.success
                    return bear, success
                else: 
                    message = bearObjSet.message
                    success = bearObjSet.success
                    return message, success
            else: 
                message = keyObj.error
                success = keyObj.success
                return message, success
                    
