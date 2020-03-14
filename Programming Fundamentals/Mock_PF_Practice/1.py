list1=["a:1234512345","b:123457890", "c:5432154321", "d:9874563210","e:9874598745"]
list2=[]
for i in list1:
    a=i.split(":")
    c=list(map(int,(a[1][:5])))
    d=list(map(int,a[1][5:]))
    
    if(sum(c)==sum(d)):
        list2.append(a[0])