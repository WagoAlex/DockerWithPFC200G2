
import json
import requests
#________________________________________________________________________________________________

myWagoCloudPassword='<>'
myWagoCloudLogin = '<>'

sURL_login = 'https://cloud.wago.com/api/token'
sHEAD_login = {"Content-type": "application/x-www-form-urlencoded"}
payload = 'grant_type=password&username='+myWagoCloudLogin+'&password='+myWagoCloudPassword

ret = requests.post(sURL_login,headers=sHEAD_login,data= payload)
#print("Login Code:",ret.status_code)
json_login_data = ret.text
obj_json_login_data = json.loads(json_login_data)

sAccess_token = obj_json_login_data["access_token"]
sName = obj_json_login_data["name"]
sID = obj_json_login_data["Id"]
sTokenType = obj_json_login_data["token_type"]
sExpires_in = obj_json_login_data["expires_in"]
sHeaderEntry = {'Authorization': sTokenType+" "+sAccess_token,'Content-Type':'application/json'}
#________________________________________________________________________________________________

sURL_data_from_device = 'https://cloud.wago.com/API/v1/jobs'

#___________________Start Edit here_____________________________________________________________________________

sYear  = "2019"

sMonth = "08"

sDayStart = "06"
sDayStop  = "06"

sHourStart = "07"
sHourStop  = "18"


myTenantID =    '9416533f-c17d-4578-90cf-42fae32d3fca'  #"793cef0d-4a52-478f-a9ae-5437a7edcfbb"
myTestDeviceID ='a759dfc5-1761-44bd-96f7-83f1370912bb'  #"c3006a0a-c218-4a65-b30c-ea1d5d2188ac" 
myProjectID =   '711a77f9-28f2-482c-8440-76cc51c45f1d'  #"5df584bf-f25d-4dac-ab9a-2e3c93b51f7c" 

tagKeys =['Office_temperature','Coffee_Level']#["Temperatur","Spannungsgeber","Netzspannung","Wirkenergie"]

myGroupKeyID= '1'
#___________________Stop Edit here_____________________________________________________________________________


sIntervalStart =sYear+"-"+sMonth+"-"+sDayStart+"T"+sHourStart+":00:00.000Z"
sIntervalStop  = sYear+"-"+sMonth+"-"+sDayStop+"T"+sHourStop+":00:00.000Z"
sFileName = "MyFile_"+sDayStart
sJobName = "myCSV_ExportJob_"+sYear+"_"+sMonth+"_"+sDayStart


myTestDevice ={
    "jobName": sJobName,
    "isScheduledJob": False,
    "interval": "1:0:0",
    "offset": "0:0:0",
    "dataExportConfig": {
        "intervalStart": sIntervalStart,
        "intervalEnd": sIntervalStop,
        "delimiter": "Semicolon",
        "tagExportHeader": sJobName,
        "additionalProperty": "",
        "datetimeFormat": "MM/dd/yyyy HH:mm:ss.fff",
        "fileNamePattern": "<p style=\"white-space: nowrap; overflow: hidden;\"><span name=\"dynamicTag\" key=\"deviceName\" contenteditable=\"false\" style=\"font-weight: bold;pointer-events: none\">{Gerätename}</span>_<span name=\"dynamicTag\" key=\"timeRange\" contenteditable=\"false\" style=\"font-weight: bold;pointer-events: none\">{Zeitraum}</span></p>",
        "useDeviceTimezone": False,
        "deviceReference": {
            "deviceId": myTestDeviceID,
            "projectId": myProjectID,
            "groups": [
                {
                    "groupKey": myGroupKeyID,
                    "tagKeys": tagKeys
                }
            ]
        }
    },
    "tenantId":myTenantID
}
json_payload_get_data_from_device = json.dumps(myTestDevice)
ret_link_data_export_d = requests.post(sURL_data_from_device,
                           headers=sHeaderEntry,
                           data= json_payload_get_data_from_device) 
#print("Export CSV File Code: ",ret_link_data_export_d.status_code)
print(ret_link_data_export_d.text)

