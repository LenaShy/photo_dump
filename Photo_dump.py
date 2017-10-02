import json
import requests


filename = "/home/lena/PycharmProjects/json_photo"
myfile = open(filename, 'r')
json_data = json.load(myfile)
i = 1
req = requests.get('http://example.com')

for item in json_data:
    #print(str(item["attachment"]["photo"]["photo_807"]))
    myfile2 = open("/home/lena/PycharmProjects/photo/" + str(i) + ".jpg", 'wb')
    if "photo_2560" in item["attachment"]["photo"]:
        req = requests.get(str(item["attachment"]["photo"]["photo_2560"]))
    elif "photo_1280" in item["attachment"]["photo"]:
        req = requests.get(str(item["attachment"]["photo"]["photo_1280"]))
    elif "photo_807" in item["attachment"]["photo"]:
        req = requests.get(str(item["attachment"]["photo"]["photo_807"]))
    elif "photo_604]" in item["attachment"]["photo"]:
        req = requests.get(str(item["attachment"]["photo"]["photo_604"]))

    myfile2.write(req.content)
    myfile2.close()
    i += 1


myfile.close()
