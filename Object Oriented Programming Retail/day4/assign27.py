#OOPR-Assgn-27
#This class represents ThemePark
class ThemePark:
    #dict_of_games contains the game name as key, 
    #price/ride and points that can be earned by customer in a list as value
    dict_of_games={'Game3': [122.0, 11], 'Game4': [60.0, 4],'Game5':[25.0, 6],
                   'Game1': [30.5, 4], 'Game2': [45.0, 8]}
    @staticmethod
    def validate_game(game_input):
        if(game_input in ThemePark.dict_of_games):
            return True
        else:
            return False
        #Remove pass and write the logic here
        #If game_input is present in ThemePark, return true. Else, return false.
    @staticmethod
    def get_points(game_input):
        return ThemePark.dict_of_games[game_input][1] 
        #Return the points that can be earned for the given game_input.
    @staticmethod
    def get_amount(game_input):
        return ThemePark.dict_of_games[game_input][0]
        #Remove pass and write the logic here
        #Return the price/ride for the given game_input

#This class represents ticket
class Ticket:
    __ticket_count=200
    def __init__(self):
        self.__ticket_id=None
        self.__ticket_amount=0
    def generate_ticket_id(self):
        Ticket.__ticket_count+=1
        self.__ticket_id=Ticket.__ticket_count
        #Auto-generate ticket_id starting from 201
    def calculate_amount(self, list_of_games):
        '''Validate the games in the list_of_games.
        If all games are valid, calculate total ticket amount and assign 
        it to attribute,ticket_amount and return true. Else, return false'''
        total=0
        count=0
        for i in list_of_games:
            if(ThemePark.validate_game(i)):
                count+=1
        if(count==len(list_of_games)):
            for i in list_of_games:
                total+=ThemePark.get_amount(i)
            self.__ticket_amount=total
            return True
        else:
            return False

    def get_ticket_id(self):
        return self.__ticket_id
    def get_ticket_amount(self):
        return self.__ticket_amount

class Customer:
    def __init__(self,name,list_of_games):
        self.__name=name
        self.__list_of_games=list_of_games
        self.__ticket=Ticket()
        self.__points_earned=0
        self.__food_coupon="No"
  
    def play_game(self):
        if("Game3" in self.__list_of_games):
            ThemePark.dict_of_games["Game2"][0]=0
            self.__list_of_games.append("Game2")
            #self.__points_earned+=ThemePark.get_points("Game2")
        for i in self.__list_of_games:
            if i in ThemePark.dict_of_games:
                self.__points_earned+=ThemePark.get_points(i)
    
    def update_food_coupon(self):
        if("Game4" in self.__list_of_games and self.__points_earned>15):
            self.__food_coupon="Yes"
    
    def book_ticket(self):
        a=self.__ticket.calculate_amount(self.__list_of_games)
        if(a>0):
            self.__ticket.generate_ticket_id()
            self.play_game()
            self.update_food_coupon()
            return True
        else:
            return False
          
    def get_name(self):
        return self.__name

    def get_list_of_games(self):
        return self.__list_of_games


    def get_ticket(self):
        return self.__ticket


    def get_points_earned(self):
        return self.__points_earned


    def get_food_coupon(self):
        return self.__food_coupon

cus1=Customer("Rahul",["Game1", "Game3"])
cus1.book_ticket()

'''Represent customers and display all details of the customer, 
if he is able to book the ticket and play the game. 
Else, display appropriate error message '''