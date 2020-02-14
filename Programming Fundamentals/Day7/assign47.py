#PF-Assgn-47

def encrypt_sentence(sentence):
    list1=sentence.split()
    for i in range(len(list1)):
        #print(type(list1[i]))
        if(i%2==0):
            list1[i]=list1[i][::-1]
        else:
            for j in list1[i]:
                if(j in 'aeiou'):
                    list1[i]=list1[i].replace(j,"")
                    list1[i]+=j
    return " ".join(list1)
                    
sentence="the sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)