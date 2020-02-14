#PF-Assgn-48

def find_correct(word_dict):
    list1=[]
    count1=0
    count2=0
    count3=0

    for i in word_dict:
        #print(word_dict[i])
        if(word_dict[i]==i):
            count1+=1
        else:
            if(len(i)!=len(word_dict[i])):
                count3+=1
            else:
                #words=zip(i,word_dict[i])
                count4=0
                for m in range(len(i)):
                    if(i[m]!=word_dict[i][m]):
                        count4+=1
                #count4=len([c for c,d in words if c!=d])
                if(count4<=2):
                    count2+=1
                else:
                    count3+=1
                '''
                k=set(i)|set(word_dict[i])
                for j in (word_dict[i]):
                    if(j not in i and i not in j):
                        count2+=1
                '''
    list1.append(count1)
    list1.append(count2)
    list1.append(count3)
    return (list1)
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))