import json
import requests
import pandas as pd
import time
import pymongo
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["miracleplus"]
mycol = mydb["professors"]

f = open("message.html", encoding="utf-8")
html = f.read()
f.close()

i = 1
for entry in mycol.find({"sent": 0, "is_valid": 1}):
    request = requests.post(
        "https://api.mailgun.net/v3/MIRACLEPLUS_EMAIL_HERE",
        auth=("api", "API_HERE"),
        data={
            "from": "奇绩创坛 <info@mail2.miracleplus.com>",
            "to": entry["email"],
            "subject": "您好{0}博士，陆奇博士奇绩创坛Reach Out".format(entry["lastname"]),
            "html": html.format(entry["lastname"], entry["institution"]),
            "h:Reply-To": "amy@mail.miracleplus.com"
        }
    )
    try:
        result = json.loads(request.text)
        if result['message'] == "Queued. Thank you.":
            mycol.update_one(entry, {"$set": {"sent": 1}})
            print("{0} {1} {2}".format(i, entry["email"], result))
            time.sleep(3)
            i += 1
        else:
            break
    except:
        break
