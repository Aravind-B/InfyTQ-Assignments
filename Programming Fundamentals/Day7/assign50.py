#PF-Assgn-50

def sms_encoding(data):
    list1=list(data.split())
    for i in range(len(list1)):
        for j in list1[i]:
            if(j in 'aeiouAEIOU'):
                if(len(list1[i])==1):
                    continue
                else:
                    list1[i]=list1[i].replace(j,"")
    return " ".join(list1)

data="I love Python"
print(sms_encoding(data))