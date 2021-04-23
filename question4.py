import json
dic={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4}

dic2={}
for i in dic:
    s=dic[i]
    for j in dic:
        a=dic[j]
        if s>a:
            dic2[j]=a
print(dic2)

file=open("ques4.json","w")
json.dump(dic2,file)
file.close()



