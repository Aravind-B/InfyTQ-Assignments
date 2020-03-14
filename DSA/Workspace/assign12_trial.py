class Stack:    
#############################################

    def __init(self,ball_stack):
        self.ball_container=ball_stack
        self.red_balls_container=[]
        self.blue_balls_container=[]
        self.green_balls_container=[]
        self.yellow_balls_container=[]
        
    def grouping_based_on_color(self):
        while(not self.ball_container.is_empty()):
            a=self.ball_container.pop()
            if(a.get_color()=="Red"):
                self.red_balls_container.append(a)
            elif(a.get_color()=="Blue"):
                self.blue_balls_container.append(a)
            elif(a.get_color()=="Yellow"):
                self.yellow_balls_container.append(a)
            else:
                self.green_balls_container.append(a)
        
        
    
    def rearrange_balls(self,color):
        if(self.red_balls_container[0].get_name()!="A"):
            self.red_balls_container[0],self.red_balls_container[1]= \
            self.red_balls_container[1],self.red_balls_container[0]
                
        if(self.blue_balls_container[0].get_name()!="A"):
            self.blue_balls_container[0],self.blue_balls_container[1]= \
            self.blue_balls_container[1],self.blue_balls_container[0]
            
        if(self.yellow_balls_container[0].get_name()!="A"):
            self.yellow_balls_container[0],self.yellow_balls_container[1]= \
            self.yellow_balls_container[1],self.yellow_balls_container[0]
            
        if(self.red_balls_container[0].get_name()!="A"):
            self.red_balls_container[0],self.red_balls_container[1]= \
            self.red_balls_container[1],self.red_balls_container[0]
            
    def display_ball_details(self,color):
        if(color=="Red"):
            b=self.red_balls_container
        elif(color=="Blue"):
            b=self.blue_balls_container
        elif(color=="Yellow"):
            b=self.yellow_balls_container
        else:
            b.self.green_balls_container
        
        b.display()        
