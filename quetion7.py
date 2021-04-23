
import json
# file to convert
file="amisha.txt"
# create a dictionary where the data will be store
dic={}
with open(file) as fn:
    for d in fn:
        # read lines from file and trim spaces to get vailed words only
        key,decs=d.strip().split(None,1)
        dic[key]=decs.strip()

# now the dictionary has been created lets convert it in json file 
otfile=open("question7.json","w")
json.dump(dic,otfile)
otfile.close()
