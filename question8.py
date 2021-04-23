import json
a=["amisha",20,"ab"]
v=["neha",20,"cd"]
dic1=["name","age","job"]
dic={}
emp1={}
emp2={}
# dic["name"]={a[0]}
# print(dic)
    
for i in range(0,len(a)):
    emp1[dic1[i]]=a[i]
for j in range(0,len(v)):
    emp2[dic1[j]]=v[j]
dic["emp1"]=emp1
dic["emp2"]=emp2
print(dic)

file1=open("question7.json","w")
json.dump(dic,file1)
file1.close()