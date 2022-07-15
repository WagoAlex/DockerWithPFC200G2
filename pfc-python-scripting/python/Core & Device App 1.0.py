

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
#print(json_login_data)

sHeaderEntry = {'Authorization': sTokenType+" "+sAccess_token,'Content-Type':'application/json',
               'api-key':'<>'}
#________________________________________________________________________________________________




workspiaceId = 'd1f9dbe7-ae52-43ac-b217-37eba631eaab'
sURL_device_command = 'https://cloud.wago.com/api/core/workspaces/'+workspiaceId+'/structure?api-version=1.0'
 
payload = {
  "parentId": "00000000-0000-0000-0000-000000000000",
  "name": "MyFolderFromAPI01"
}

json_payload = json.dumps(payload)

ret_folder = requests.post(sURL_device_command,
                            
                            headers=sHeaderEntry,
                            data= json_payload,
                            )

#print("Response Code",ret_folder.status_code)
print(ret_folder.text)



myTestDeviceID='a759dfc5-1761-44bd-96f7-83f1370912bb' 

workspiaceId = 'd1f9dbe7-ae52-43ac-b217-37eba631eaab'
sURL_device_command = 'https://cloud.wago.com/api/deviceapp/devices?workspaceId='+workspiaceId+'&api-version=1.0'
 
payload = {

"folderId": "00000000-0000-0000-0000-000000000000",
 "deviceName": "YourDeviceFromAPI01"
}

json_payload_device = json.dumps(payload)

ret_device_d = requests.post(sURL_device_command,
                            headers=sHeaderEntry,
                            data= json_payload_device,
                            )

#print("Response Code",ret_device_d.status_code)
print(ret_device_d.text)




