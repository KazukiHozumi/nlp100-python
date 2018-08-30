import json
import re

def getUkText():
    with open("jawiki-country.json") as f:
        article = f.readline()
        for line in f:
            json_dict = json.loads(line)
            if json_dict["title"] == "イギリス":
                return json_dict["text"]

lines = getUkText().split("\n")

for line in lines:
    section_line = re.search("^(=+)\s*(.*?)\s*(=+)$", line)
    if section_line is not None:
        print(section_line.group(2), len(section_line.group(1)) - 1)
