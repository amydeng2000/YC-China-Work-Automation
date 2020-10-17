import requests
import json
import pandas as pd

payload = [
    {
        "action": "conf.GetAuthors",
        "parameters": {
            "conf_id": "5eda155192c7f9be21cd1a13",
            "offset": 0,
            "size": 20,
            "category": None,
            "language": 1
        },
        "schema": {
            "authors": [
                "id",
                "name",
                "title",
                "titles",
                "name_zh",
                "avatar",
                "tags",
                {
                    "profile": [
                        "position",
                        "position_zh",
                        "affiliation",
                        "affiliation_zh",
                        "org",
                        "org_zh"
                    ]
                },
                {
                    "indices": [
                        "hindex",
                        "gindex",
                        "pubs",
                        "citations",
                        "newStar",
                        "risingStar",
                        "activity",
                        "diversity",
                        "sociability"
                    ]
                },
                "person.indices.activity",
                "person.indices.citations",
                "person.indices.citation",
                "person.indices.diversity",
                "person.indices.gindex",
                "person.indices.hindex",
                "person.indices.newStar",
                "person.indices.pubs",
                "person.indices.numpubs",
                "contact.position",
                "contact.position_zh",
                "contact.affiliation",
                "contact.affiliation_zh",
                "contact.org",
                "contact.org_zh"
            ]
        }
    }
]
headers = {
    "Content-Type": "application/json"
}

output = []
for i in range(0, 620, 20):
    payload[0]['parameters']['offset'] = i
    url = "https://apiv2.aminer.cn/magic?a=GetAuthors__conf.GetAuthors___"
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))
    response.encoding = "utf8"
    try:
        data = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        print(response.text)
        break
    items = data['data'][0]['items']
    for item in items:
        entry = {
            "name": item['name'],
            "name_zh": item['name_zh'] if 'name_zh' in item.keys() else "",
            "affiliation": item['profile']['affiliation'] if 'profile' in item.keys() and 'affiliation' in item['profile'].keys() else "",
            "id": item['id']
        }
        output.append(entry)
    print("offset {0} finished".format(i))

output = pd.DataFrame(data=output)
# output.to_csv("aminerstudents.csv", index=False, encoding='utf-8')
