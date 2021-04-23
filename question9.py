import json
shopping_list={ 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        }

print(shopping_list)
user=input("which item do you want to purches")
for i in shopping_list:
    if i==user:
        print(user,shopping_list[i])
item=int(input("how many items you want"))
out = dict(list(shopping_list.items())[0: item]) 
print(out)
file1=open("question","w")
json.dump(out,file1)
file1.close()

    
# add=input("would you like to add some items")
# file1=open("question7","w")
# json.dump(shopping_list,file1)
# file1.close()

