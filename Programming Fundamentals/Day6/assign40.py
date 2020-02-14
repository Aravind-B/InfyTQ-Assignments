#PF-Assgn-40

def is_palindrome(word):
    word=word.lower()
    if(not word[0]==word[-1]):
        return False
    else:
        if(len(word)<=2):
            return True
        return is_palindrome(word[1:-1])

#Provide different values for word and test your program
result=is_palindrome("M am")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
