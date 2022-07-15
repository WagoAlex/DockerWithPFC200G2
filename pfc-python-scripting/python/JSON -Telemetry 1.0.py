

myWagoCloudPassword='<>'
myWagoCloudLogin = '<>'


import json
import requests
#________________________________________________________________________________________________

sURL_login = 'https://cloud.wago.com/api/token'
sHEAD_login = {"Content-type": "application/x-www-form-urlencoded"}
payload = 'grant_type=password&username='+myWagoCloudLogin+'&password='+myWagoCloudPassword


ret = requests.post(sURL_login,headers=sHEAD_login,data= payload)
print("Login Code:",ret.status_code)
json_login_data = ret.text
obj_json_login_data = json.loads(json_login_data)

sAccess_token = obj_json_login_data["access_token"]
sTokenType = obj_json_login_data["token_type"]
sHeaderEntry = {'Authorization': sTokenType+" "+sAccess_token,'Content-Type':'application/json',
               'api-key':'<>'}
#_________________________________________________________________________________________________


StartTime = "StartTime=2019-08-06T08:00:00"
EndTime= "EndTime=2019-08-06T19:00:00"
mySingleTagKey = 'Office_temperature'
myTestDeviceID='a759dfc5-YYYY-ZZZZ-96f7-83f1370912bb' 
#_________________________________________________________________________________________________

sURL_data_from_device_history = 'https://cloud.wago.com/api/telemetry/telemetrydata/raw?'+StartTime+'&'+EndTime+'&api-version=1.0'

myPayload = [
                {
                "deviceId": myTestDeviceID,
                "collectionKey": "1",
                "tagKey":mySingleTagKey
                }
           ]



json_payload_get_raw_data_ = json.dumps(myPayload)
ret_raw_data = requests.post(sURL_data_from_device_history,
                           headers=sHeaderEntry,
                           data= json_payload_get_raw_data_)

print("Code: ",ret_raw_data.status_code)
print("Response: ",ret_raw_data.text)

