#DSA-Assgn-5

from day2.DataStructures import LinkedList

def create_new_sentence(word_list):
    new_sentence=""
    temp=word_list.get_head()
    while(temp!=None):
        if(temp.get_data()=="*" or temp.get_data()=="/"):
            #temp.set_data(" ")
            if(temp.get_next().get_data()=="*" or 
               temp.get_next().get_data()=="/"):
                temp=temp.get_next()
                temp.get_next().set_data(temp.get_next().get_data().upper())
            new_sentence+=" "
        else:
            new_sentence+=temp.get_data()
        temp=temp.get_next()
    return new_sentence  
        

word_list=LinkedList()
word_list.add("T")
word_list.add("h")
word_list.add("e")
word_list.add("/")
word_list.add("*")
word_list.add("s")
word_list.add("k")
word_list.add("y")
word_list.add("*")
word_list.add("i")
word_list.add("s")
word_list.add("/")
word_list.add("/")
word_list.add("b")
word_list.add("l")
word_list.add("u")
word_list.add("e")
print(word_list.__str__())
result=create_new_sentence(word_list)
print(result)
