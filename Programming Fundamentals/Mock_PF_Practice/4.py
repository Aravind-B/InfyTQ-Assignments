string = "IND-USA-PAK/AUS-FSD-IND/FSD-IND-GVF"
dict1 = {}
string = string.replace("/", "-")
list1 = string.split("-")

for i in range(len(list1)):
    dict1[list1[i]]=[]
    
for i in range(len(list1)):
    if(list1[i] in dict1):
        dict1[list1[i]].append(i+1)
print(dict1)
            