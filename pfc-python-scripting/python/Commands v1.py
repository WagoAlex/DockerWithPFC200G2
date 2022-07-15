
myWagoCloudPassword='<>'
myWagoCloudLogin = '<>'



import requests
import json 


sURL_login = 'https://cloud.wago.com/api/token'
sHEAD_login = {"Content-type": "application/x-www-form-urlencoded"}
payload = 'grant_type=password&username='+myWagoCloudLogin+'&password='+myWagoCloudPassword



ret = requests.post(sURL_login,headers=sHEAD_login,data= payload)
print("Login Code:",ret.status_code)

json_login_data = ret.text
obj_json_login_data = json.loads(json_login_data)

sAccess_token = obj_json_login_data["access_token"]
sName = obj_json_login_data["name"]
sID = obj_json_login_data["Id"]
sTokenType = obj_json_login_data["token_type"]
sExpires_in = obj_json_login_data["expires_in"]
print(json_login_data)

sHeaderEntry = {'Authorization': sTokenType+" "+sAccess_token,'Content-Type':'application/json'}

#________________________________________________________________________________________________



myTestDeviceID='a759dfc5-1761-44bd-96f7-83f1370912bb' 

sURL_device_command = 'https://cloud.wago.com/API/v1/devices/'+myTestDeviceID+'/commands'

ret_get_commands_d = requests.get(
                        sURL_device_command,
                        headers=sHeaderEntry)
#print(ret_get_commands_d.text)
json_ret_get_commands_d = json.dumps(ret_get_commands_d.text)
print("Get commands Code:",ret_get_commands_d.status_code)
print("Get commands Response:",ret_get_commands_d.text)


#________________________________________________________________________________________________


myTestDeviceID='a759dfc5-1761-44bd-96f7-83f1370912bb'

sURL_device_command = 'https://cloud.wago.com/API/v1/devices/'+myTestDeviceID+'/commands'
#
payload_command_1 = {
    "CommandId": 1,
    "CommandTimeout": 60000,#ms
    "CommandParameters": [
                            {
                            "Name": "Floating Value",
                            "Value": 42.42
                            }
                        ]
}
json_payload_command_1 = json.dumps(payload_command_1)

ret_set_commands_d = requests.post(
                            sURL_device_command,
                            headers=sHeaderEntry,
                            data= json_payload_command_1)

print("Code",ret_set_commands_d.status_code)
print("Response",ret_set_commands_d.text)

