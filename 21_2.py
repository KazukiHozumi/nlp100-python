from mymodule import extract_from_json

lines = extract_from_json(u"イギリス").split("\n")

for line in lines:
    if "Category" in line:
        print(line)
