import turtle           # allows us to use the turtles library
wn = turtle.Screen()    # creates a graphics window
wn.setup(500,500)       # set window dimension

alex = turtle.Turtle()  # create a turtle named alex
alex.shape("turtle")    # alex looks like a turtle


'''
alex.color("black")    # alex has a color
alex.right(60)         # alex turns 60 degrees right
alex.left(60)          # alex turns 60 degrees left
alex.circle(50)        # draws a circle of radius 50
#draws circles
for counter in range(1,3):
    alex.circle(20*counter)
'''
alex.color('red')
alex.left(120)
alex.circle(50)
for counter in range(1,4):
    alex.circle(20*counter)
 
alex.color('green')
alex.right(120)
alex.circle(50)
for counter in range(1,4):
    alex.circle(20*counter)
    
alex.color('blue')
alex.right(120)
alex.circle(50)
for counter in range(1,4):
    alex.circle(20*counter)
#Write the logic to create the given pattern
#Refer the statements given above to draw the pattern
