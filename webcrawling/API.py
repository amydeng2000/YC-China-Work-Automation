import json
import requests

"""
AIRTABLE API WITH PYTHON REQUESTS
*************************************

Request URL follows the same format: 
https://api.airtable.com/v0/{{BASE_ID}}/{{TABLE_NAME}}/{{OPTIONAL_RECORD_ID}}?{{API_KEY}}

>>> sample_record_url = "https://api.airtable.com/v0/appUgZme5vJ9ddNTR/test/recUcPkiH86Rb6dY7?api_key=keyoAXinPEwmZVepb"
>>> table_url = "https://api.airtable.com/v0/appUgZme5vJ9ddNTR/test?api_key=keyoAXinPEwmZVepb"
>>> headers = {"Content-Type": "application/json"}



AIRTABLE DATA STRUCTURE
**************************

Airtable is essentially a NoSQL database. 
Each record is a dictionary of keys and records. If a field is empty, the key doesn't exist.
Record_ID is unique to a row in the airtable. Adding rows below and after won't change the ID,
but cutting a row of record and pasting it in a new row will change its ID.
"""



"""
CREATING A NEW RECORD
*************************

new_record = {
    "records": [
        {
            "fields": {
                "Name": "jack",
                "gender": "male",
                "occupation": "VC"
            }
        },
        {
            "fields": {
                "Name": "Jess",
                "gender": "female",
                "occupation": "HR"
            }
        }
    ]
}
response = requests.request("POST", table_url, headers=headers, data=json.dumps(new_record))



CHANGE A FIELD OF A RECORD
******************************

update = {
    "records": [
        {
            "id": "recUcPkiH86Rb6dY7",
            "fields": {
                "Name": "amy",   # Not changing this field
                "occupation": "CHANGED",    # Changing this field
            }
        }
    ]
}
response = requests.request("PATCH", table_url, headers=headers, data=json.dumps(update))

SAMPLE RESPONSE
{
    "id":"recUcPkiH86Rb6dY7",
    "fields":{
        "项目链接1":
            {"label":"犀牛数据","url":"https://www.xiniudata.com/search2?name=amy"},
        "项目链接2":
            {"label":"企名片","url":"https://www.qimingpian.cn/searchresult?wd=amy"},
        "Name":"amy",
        "gender":"F",
        "occupation":"Intern",
        "phone number":"15611947467",
        "Field 7":2},
    "createdTime":"2020-08-05T07:33:21.000Z"
}



RETRIEVING A RECORD
************************
response = requests.request("GET", sample_record_url, headers=headers)

SAMPLE RESPONSE
{
    "id":"recUcPkiH86Rb6dY7",
    "fields":{
        "项目链接1":
            {"label":"犀牛数据","url":"https://www.xiniudata.com/search2?name=amy"},
        "项目链接2":
            {"label":"企名片","url":"https://www.qimingpian.cn/searchresult?wd=amy"},
        "Name":"amy",
        "gender":"F",
        "occupation":"Intern",
        "phone number":"15611947467",
        "Field 7":2},
    "createdTime":"2020-08-05T07:33:21.000Z"
}
"""


temp_url ="https://api.airtable.com/v0/appUgZme5vJ9ddNTR/test?api_key=keyoAXinPEwmZVepb"
headers = {"Content-Type": "application/json"}
# params={'fields': ['项目名称', '创始人姓名']}
params={'fields': ['项目名称']}
formulas = ""
response = requests.request("GET", temp_url, headers=headers, params=params, formula=formulas)
response.encoding = "utf8"
print(json.loads(response.text))



# params={'fields': ['FieldOne', 'FieldTwo']}
# params={'sort': ['FieldOne', '-FieldTwo']}
# params={'sort': [('FieldOne', 'asc'), ('-FieldTwo', 'desc')]}





# try:
#     data = json.loads(response.text)
# except json.decoder.JSONDecodeError:
#     print(response.text)
