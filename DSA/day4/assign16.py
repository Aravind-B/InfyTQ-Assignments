#DSA-Assgn-16

from day2.DataStructures import Stack,Queue

def separate_boxes(box_stack):
    new_queue=Queue(box_stack.get_max_size())
    list1=[]
    while(not box_stack.is_empty()):
        a=box_stack.pop()
        if(a not in ["Red","Green","Blue"]):
            new_queue.enqueue(a)
        else:
            list1.append(a)
    for i in list1[::-1]:
        box_stack.push(i)
    return new_queue

#Use different values for stack and test your program
box_stack=Stack(8)
box_stack.push("Red")
box_stack.push("Magenta")
box_stack.push("Yellow")
box_stack.push("Red")
box_stack.push("Orange")
box_stack.push("Green")
box_stack.push("White")
box_stack.push("Purple")
print("Boxes in the stack:")
box_stack.display()
result=separate_boxes(box_stack)
print()
print("Boxes in the stack after modification:")
box_stack.display()
print("Boxes in the queue:")
result.display()
