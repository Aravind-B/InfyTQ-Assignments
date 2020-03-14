dict1={'ram':31,'shyam':56,'karan':38,'sandy':75,'shruti':190}

list1=[]
for key,value in dict1.items():
    if(value>35):
        for j in key:
            if(j in 'aeiou'):
                list1.append(key.replace(j,""))

print(list1)