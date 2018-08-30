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
    file_line = re.search(u"(File|ファイル):(.*?)\|", line)
    if file_line is not None:
        print(file_line.group(2))
