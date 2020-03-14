def change_making(amount, denominations):
    d=sorted(denominations, reverse=True)
    count=0
    
    while(amount!=0 and len(d)>0):
        if(d[0]<=amount):
            amount-=d[0]
            count+=1
        else:
            d=d[1:]
        
    if(amount==0):
        return count
    else:
        return -1
        
    
deno=[15,10,1]
print(change_making(20, deno))

    
