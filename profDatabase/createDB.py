import pymongo
import pandas as pd
import numpy as np
import requests
import json

# connect to MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["miracleplus"]
mycol = mydb["professors"]


def is_eng(uchar):
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False


def get_lastname(name):
    if is_eng(name):
        lastname = name.split()[-1]
        if lastname[0] == "(" or lastname[0] == "（":
            lastname = lastname[1]
        elif "(" in lastname:
            k = lastname.index("(")
            lastname = lastname[:k]
        elif "（" in lastname:
            k = lastname.index("（")
            lastname = lastname[:k]
    else:
        lastname = name[0]
    return lastname


# Use mailgun API to test the validity of the emails
def test_email(email, count):
    url = "http://www.mail-verifier.com/do/api/?key=D562BC469E9BCC5CE98A04D7273B3297&verify={0}".format(email)
    response = requests.request("GET", url)
    result = json.loads(response.text)["code"]
    if result == 1:
        return result
    elif (result == 0 or result == -5) and count < 2:
        count += 1
        return test_email(email, count)
    else:
        return result


# import data
data = pd.read_csv("SAMPLE_IEEE.csv").T.to_dict()
for i in range(len(data)):
    entry = data[i]
    if entry["name"] is not np.nan \
            and entry["institution"] is not np.nan\
            and entry["email"] is not np.nan:
        email = entry["email"].strip()
        name = entry["name"].strip()
        institution = entry["institution"].strip()
        myquery = {"email": email}
        if mycol.find(myquery).count() == 0:
            lastname = get_lastname(name)
            is_valid = test_email(email, 0)
            dict = {
                "name": name,
                "lastname": lastname,
                "institution": institution,
                "email": email,
                "validated": 1,
                "is_valid": is_valid,
                "sent": 0
                # "bio": 1
            }
            mycol.insert_one(dict)
            print("{0} {1} {2} {3}".format(i, dict["name"], dict["email"], dict["is_valid"]))



"""
*** RECYCLABLE CODE PIECES ***

#Delete Repetitions
--------------------
for x in mycol.find():
    if mycol.find(x) is not None:
        print(x["name"])
        mycol.delete_one(x)


#Get number of entry entries
----------------------------
print(mycol.count())


#Change a filed name
---------------------
mycol.update_many( {}, { "$rename": { "firstname": "lastname" } } )


#Change the value of an entry
-----------------------------
for x in mycol.find():
    mycol.update_one(x, {"$set": {"lastname": get_lastname(x["name"])}})


#Delete a field
-----------------
mycol.update_one({"email": "caining@mail.xidian.edu.cn"}, {"$unset": {"firstname": ""}})

"""