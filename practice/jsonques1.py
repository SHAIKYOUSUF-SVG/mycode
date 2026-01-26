import json
with open("file1.json","r") as fr:
    json_file=json.load(fr)
print(json_file)