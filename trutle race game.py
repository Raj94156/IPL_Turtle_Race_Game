import turtle
import random
screen1 = turtle.Screen()
screen1.bgcolor("grey")
user_team = screen1.textinput(title="IPL race :MI,CSK,KKR,RCB ",prompt="Which is your team:choose jersey color")
screen1.setup(width=500,height=400)
#Initial turtle position list
y_pos=[-40,-10,20,50]
#color list
color1 = ["red","yellow","purple","blue"]
#list for appending turtles
ipl_team = []
for turtle_index in range(0,4):
    ipl = turtle.Turtle()
    ipl.shape("turtle")
    ipl.penup()
    ipl.goto(x=-250,y=y_pos[turtle_index])
    ipl.color(color1[turtle_index])
    ipl_team.append(ipl)
if user_team:
    is_race_on= True
while is_race_on:
    for team in ipl_team:
        if team.xcor()>230:
            is_race_on = False
            winner_color = team.pencolor()
            if winner_color == user_team:
                print(f"you have won the race ,Your Team jersey color is {winner_color}")
            else:
                print(f"you have lose the race ,Your Team jersey color is {winner_color}")



        random_walk=random.randint(0,10)
        team.forward(random_walk)
