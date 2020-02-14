from itertools import permutations,combinations
def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
    #Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    
    list1=[]
    str1=str(num)
    a=permutations(str1,len(str1))
    for i in set(a):
        if(''.join(i) not in list1):
            list1.append(int(''.join(i)))
    list1.sort()
    '''
    list1=[]
    str1=str(num)
    str2=""
    for i in range(len(str1)-1):
        str2+=str1[i+1]
        
    str2+=str1[0]
    str1=str2
    list1.append(num)
    list1.append(int(str2))
    '''
    b=combinations(list1,3)
    for j in b:
        print(b)
    return combinations(list1,2)
num=179

res=rotations(num)