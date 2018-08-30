import json

def getUkText():
    with open("jawiki-country.json") as f:
        article = f.readline()
        for line in f:
            json_dict = json.loads(line)
            if json_dict["title"] == "イギリス":
                return json_dict["text"]

lines = getUkText().split("\n")

for line in lines:
    if "Category" in line:
        print(line)