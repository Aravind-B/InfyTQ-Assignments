
# Linear Search
l1 = ["Abc",
      "Bcd",
      "Cde",
      "Def",
      "Defg"]

def hash_func(data1):
    key=data1[0].upper()
    return key

dict1={}

 

for name in l1:
    k=hash_func(name)
    if k in dict1.keys():
        dict1[k].append(name)
    else:
        dict1[k]=[name]
    '''
    try:
        dict1[k].append(name.upper())
    except KeyError:
        dict1[k]=[name.upper()]
        
    '''
    
for i in dict1:
    print(i,dict1[i])
print(dict1)
dict2=dict1
    
    
name="Abc"
key=hash_func(name)
l2=dict1.get(key, [])
if(name in l2):
    print("yes")
else:
    print("no")