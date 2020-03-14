
def fib(num):
    global fibo,count
    if(num<=len(fibo)-1):
        return fibo[num]
    else:
        fibo.append(fib(num-1)+fib(num-2))
        if(num==3):
            count+=1
        return fibo[num]

fibo=[]
fibo.append(0)
fibo.append(1)
count=1
n=8  
print(n,"th Fib number",fib(n))
print(count)