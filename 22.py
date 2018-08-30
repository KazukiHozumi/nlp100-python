import json

def getUkText():
    with open("jawiki-country.json") as f:
        article = f.readline()
        for line in f:
            json_dict = json.loads(line)
            if json_dict["title"] == "イギリス":
                return json_dict["text"]

import re

lines = getUkText().split("\n")

for line in lines:
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category_line is not None:
        print(category_line.group(1))
