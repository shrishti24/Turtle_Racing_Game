from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color.")

is_race_on = False

# creating a finish line
timmy = Turtle()
timmy.penup()
timmy.goto(x=230, y=180)
timmy.right(90)
timmy.pendown()
timmy.pen(pencolor="black", pensize=10)
timmy.forward(320)
timmy.penup()
timmy.ht()


colors = ["red", "yellow", "blue", "green", "violet", "orange"]
turtle_list = []
# to position our turtles to the starting line
# we make use of position argument 'goto',at home the turtle is at (0,0)
# as the width we have given is 500 so from the center 250 will be on the left hand side and same on right

coord_y = -100
for colour in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colour)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=coord_y)
    coord_y += 50
    turtle_list.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220.00:
            if turtle.pencolor() == user_input:
                print(f" YAY! YOU GUESSED IT RIGHT. {turtle.pencolor()} WON")
            else:
                print(f"SORRY! YOU LOOSE. {turtle.pencolor()} WON")
            is_race_on = False

        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
