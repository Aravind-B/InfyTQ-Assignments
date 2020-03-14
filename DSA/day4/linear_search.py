# Linear Search
l1 = [(1011, "A"),
    (1022, "B"),
    (1033, "C"),
    (1044, "D")]

# emp_no=int(input("Enter emp id"))

emp_no = 1033


found = False
for row in l1:
    if(row[0] == emp_no):
        print(row[1])
        found = True
if(not found):
    print("Not found")
    

for row in l1:
    if(row[0] == emp_no):
        print(row[1])
        break
else:
    print("Not found")
    

def l_search(n,data):
    if(row[0]==n):
        return row[1]
    return 'Not Found' 

d1={}
d1[1]=["A"]
print(d1[1].append('A'))
    