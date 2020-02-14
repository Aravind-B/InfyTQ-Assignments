#OOPR-Assgn-22
class Multiplex:
    k=0
    __list_movie_name=["movie1","movie2"]
    __list_total_tickets=[100,60]
    __list_last_seat_number=["M1-10",None]
    __list_ticket_price=[150,200]
    def __init__(self):
        self.__seat_numbers=None
        self.__total_price=None
    def calculate_ticket_price(self,movie_index,number_of_tickets):
        self.__total_price= Multiplex.__list_ticket_price[movie_index]*number_of_tickets
    def check_seat_availability(self,movie_index,number_of_tickets):
        if(Multiplex.__list_total_tickets[movie_index]<number_of_tickets):
            return False
        else:
            return True
    def get_total_price(self):
        return self.__total_price
    def get_seat_numbers(self):
        return self.__seat_numbers
    def book_ticket(self, movie_name, number_of_tickets):
        '''Write the logic to book the given number of tickets for the specified movie.''' 
        self.__seat_numbers=[]
        self.__total_price=0
        if(movie_name not in Multiplex.__list_movie_name):
            return 0
        elif(not self.check_seat_availability(Multiplex.__list_movie_name.index(movie_name),number_of_tickets)):
            return -1
        else:
            self.__seat_numbers=self.generate_seat_number(Multiplex.__list_movie_name.index(movie_name), number_of_tickets)
            self.calculate_ticket_price(Multiplex.__list_movie_name.index(movie_name), number_of_tickets)

    def  generate_seat_number(self,movie_index, number_of_tickets):
        '''Write the logic to generate and return the list of seat numbers'''
        list_of_seat_numbers=[]
        last_seat=Multiplex.__list_last_seat_number[movie_index]
        
        if(last_seat is None):
            last_seat=0
        else:
            last_seat=int(last_seat[3:])
            #print(type(last_seat))
        for i in range(1,number_of_tickets+1):
            if(movie_index==0):
                seat_num="M1"+'-'+str(last_seat+i)
            else:
                seat_num="M2"+'-'+str(last_seat+i)
            list_of_seat_numbers.append(seat_num)
            
        Multiplex.__list_total_tickets[movie_index]-=number_of_tickets
        Multiplex.__list_last_seat_number[movie_index]=list_of_seat_numbers[-1]
            
        
        '''
        list3=[]
        Multiplex.k=0
        for i in range(number_of_tickets):
            Multiplex.k+=1
            for j in Multiplex.__list_last_seat_number:
                if(j is not None):
                    #a=Multiplex.__list_last_seat_number[i]
                    m=j.split("-")
                    if(m[1].isdigit()):
                        Multiplex.k=int(m[1])
                        if(movie_index==0):
                            seat="M1-"
                        else:
                            seat="M2-"
                #k+=1
                else:
                    Multiplex.k=0
                    if(movie_index==0): 
                        seat="M1-"
                    else:
                        seat="M2-"
                #k+=1
            list3.append(seat+str(int(Multiplex.k)))
        Multiplex.__list_last_seat_number[movie_index]=list3[-1]
        Multiplex.__list_total_tickets[movie_index]-=number_of_tickets
        
        
        for i in range(number_of_tickets):
            k+=1
            if(movie_index==0):
                
                if(Multiplex.__list_last_seat_number[0] is not None):
                    a=Multiplex.__list_last_seat_number[0]
                    m=a.split("-")
                    if(m[1].isdigit()):
                        k=int(m[1])
                            
                    seat="M1-"
                else:
                    seat="M1-"
            
                #list1.append(seat+str(i))
                #Multiplex.__list_last_seat_number[0]=list1[-1]
                #print(list1[-1])
                #return list1
            else:
                if(Multiplex.__list_last_seat_number[1] is not None):
                    a=Multiplex.__list_last_seat_number[1]
                    m=a.split("-")
                    if(m[1].isdigit()):
                        k=int(m[1])
                    seat="M2-"
                    #k=(int(s) for s in seat.split('-') if s.isdigit())
                else:
                    seat="M2-"
                #list2.append(seat+str(i))
                #Multiplex.__list_last_seat_number[1]=list2[-1]
                #return list2
            list3.append(seat+str(int(k)))
        Multiplex.__list_last_seat_number[movie_index]=list3[-1]
        Multiplex.__list_total_tickets[movie_index]-=number_of_tickets
        '''
        return list_of_seat_numbers 
        
booking1=Multiplex()
status=booking1.book_ticket("movie1",10)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-1")
else:
    print("Booking successful")
    print("Seat Numbers :", booking1.get_seat_numbers())
    print("Total amount to be paid:", booking1.get_total_price())
print("-----------------------------------------------------------------------------")
booking2=Multiplex()
status=booking2.book_ticket("movie2",6)
if(status==0):
    print("invalid movie name")
elif(status==-1):
    print("Tickets not available for movie-2")
else:
    print("Booking successful")
    print("Seat Numbers :", booking2.get_seat_numbers())
    print("Total amount to be paid:", booking2.get_total_price())