#PF-Tryout
#Program to be tested

def boarding(seat_number):
    if(seat_number>=1 and seat_number<=25):
        batch_no=1
    elif(seat_number>=26 or  seat_number<=100):
        batch_no=2
    elif(seat_number>=101 and seat_number<=200):
        batch_no=3
    else:
        batch_no=-1
    return batch_no