
[0, 1, 1, 2, 3, 5, 8, 13, 21, ...]
memo = {}

def fibonacci_n(n):
    
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        val = memo.get(n, -1)
        if(val==-1):
            val= fibonacci_n(n - 1) + fibonacci_n(n - 2)
            memo[n]=val
        return val
    
    
print(fibonacci_n(6))
