#DSA-Assgn-18

def find_unknown_words(text,vocabulary):
    text_list=text.split()
    new_set=set()
    for word in text_list:
        if(word not in vocabulary):
            new_set.add(word)
    if(not new_set):
        return -1
    else:
        return new_set

#Pass different values of text and vocabulary to the 
#function and test your program
text="The sun rises in the east and sets in the west."
vocabulary = ["sun","in","rises","the","east"]
unknown_words=find_unknown_words(text,vocabulary)
print("The unknown words in the file are:",unknown_words)