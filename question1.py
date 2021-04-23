import json

a={"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
file=open("file.json","w")
json.dump(a,file)
file.close()


