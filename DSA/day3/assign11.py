#DSA-Assgn-11


from day2.DataStructures import Queue

def merge_queue(queue1,queue2):
    q1_size=queue1.get_max_size()
    q2_size=queue2.get_max_size()
    new_q_size=q1_size+q2_size
    merged_queue=Queue(new_q_size)
    
    while(new_q_size):
        q1=queue1.dequeue()
        q2=queue2.dequeue()
        if(q1 is not None and q2 is not None):
            merged_queue.enqueue(q1)
            merged_queue.enqueue(q2)
        elif(q2 is None):
            merged_queue.enqueue(q1)
        else:
            merged_queue.enqueue(q2)
        new_q_size-=1
    return merged_queue

#Enqueue different values to both the queues and test your program

queue1=Queue(3)
queue2=Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue=merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()
