list1=['ants:123', 'bulk:127','some:896','pile:627','shakti:190']
keyword='akzpi'
list2=[]
m=0
for i in list1:
    j=i.split(":")
    str1=j[0]
    num=j[1]
    sum1=0
    if(keyword[m] in str1):
        pos=str1.index(keyword[m])+1
        for k in num:
            sum1+=int(k)
        list2.append(pos*sum1)
    else:
        list2.append(0)
    m+=1
    