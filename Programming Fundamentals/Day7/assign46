#PF-Assgn-46

global s1
def nearest_palindrome(number):
    s1=str(number+1)
    if s1==s1[::-1]:
        return int(s1)
    else:
        number+=1
        return nearest_palindrome(number)
        #return s1

number=12321
print(nearest_palindrome(number))
