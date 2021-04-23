import json
file=open("file.json","r")
print(json.load(file))
file.close()