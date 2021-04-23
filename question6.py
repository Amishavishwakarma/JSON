import json
a={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
}

a=json.dumps(a)
b=json.loads(a)
print(type(b))
print(type(a))










