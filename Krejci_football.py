#Jack Krejci
#Program that creates a simulation college OT football game using turtle graphics
import turtle
import random

#Create screen and turtle to make field
win = turtle.Screen()
win.setup(850,520,532,60)
sam = turtle.Turtle()
sam.hideturtle()
sam.color("Green")
sam.speed(0)

#Create the field using a yellow outline
sam.pu()
sam.goto(-304,200)
sam.pd()
sam.begin_fill()
sam.pencolor("Yellow")
sam.pensize(5)
#Create the grass
for i in range(2):
    sam.forward(700)
    sam.right(90)
    sam.forward(400)
    sam.right(90)
sam.end_fill()

#create the lines
for i in range(3):
    sam.forward(100)
    sam.right(90)
    sam.forward(400)
    sam.left(90)
    sam.forward(100)
    sam.left(90)
    sam.forward(400)
    sam.right(90)
sam.pu()
#create the yard lines
sam.goto(-304,215)
sam.pencolor("Black")
sam.write("30",font=("Arial",10,"bold"))
sam.forward(95)
sam.write("25",font=("Arial",10,"bold"))
sam.forward(100)
sam.write("20",font=("Arial",10,"bold"))
sam.forward(100)
sam.write("15",font=("Arial",10,"bold"))
sam.forward(100)
sam.write("10",font=("Arial",10,"bold"))
sam.forward(100)
sam.write("5",font=("Arial",10,"bold"))
sam.forward(100)
sam.write("0",font=("Arial",10,"bold"))

#Create the users team
team = turtle.Turtle()
team.color("Brown")
team.shape("turtle")
team.pu()
team.goto(-204,0)

#Give user decision to pass or run
#Give values to counters which keep track of your stats
game_on = True
yard_line = 25
down = 1
yards_to_go = 10

#Writes the initial "First and 10"
sam.goto(-302,-215)
sam.write("Down 1, 10 yards to go")

#Creates loop to run or pass which stops when you win/lose
while game_on == True:
    game_plan = input("Enter r to run and p to pass: ").lower().strip()
    #Tells user if they didn't enter an r or p which also fixes the problem of a failed
    while game_plan != "p" and game_plan != "r":
        game_plan = input("That's not in the play book! Please enter r or p: ")
    #Gives action when selecting to pass
    if game_plan == "p":
        passing = random.randint(0,1)
        if passing == 0:
            print("Incomplete pass!")
        elif passing == 1:
            pass_complete = random.randint(3,15)
            yard_line -= pass_complete
            yards_to_go -= pass_complete
            turt_move = pass_complete * 20
            team.forward(turt_move)
            print("Complete pass for %d yards!" % pass_complete)
    #Gives action when selecting to run
    elif game_plan == "r":
        running = random.randint(-3,8)
        yard_line -= running
        yards_to_go -= running
        turt_move = running * 20
        team.forward(turt_move)
        print("Run for %d yards" % running)

    #Keeps track of what down your on and whether or not you advance to a first down
    down += 1
    if yards_to_go <= 0:
        down = 1
        yards_to_go = 10
    if yard_line <= 10 and down == 1:
        yards_to_go = yard_line

    #Tells you your down, where you are, and how many yards you need
        #and if you lose or win
        #also makes the turtle change what down it is with undo and if statement
    
##    sam.goto(-302,-215)
##    sam.write("Down %d, %d yards to go" % (down,yards_to_go))
    sam.undo()
    
    if down <= 4 and yard_line > 0:
        print("Down %d and %d yards to go on the %d yard line." % (down,yards_to_go,yard_line))
        sam.write("Down %d, %d yards to go" % (down,yards_to_go))
    elif yard_line <= 0:
        print("Touchdown! You Won!")
        game_on = False
    else:
        print("You ran out of downs. You lost!")
        game_on = False
#Close window when game is over
win.bye()

        

    
    














          
