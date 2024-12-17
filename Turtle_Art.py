import turtle
import random

#create two distinct turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()
#function for one turtle that takes a parameter, has a loop, an if statement, and uses random
def random_pattern(t, size):
    for i in range(36):
        t.forward(size)
        t.right(10)
        #randomize color and pen width every 5 times
        if i % 5 == 0:
            color_choice = random.choice(['red', 'green', 'blue', 'yellow', 'purple'])
            t.pencolor(color_choice)
            t.pensize(random.randint(1, 5))
#call random_pattern function twice with different parameters
random_pattern(t1, 50)
random_pattern(t2, 100)
#function to draw an interesting figure with a turtle (takes turtle as a parameter)
def draw_spiral(t):
    for i in range(100):
        t.forward(i * 3 / 2 + i)
        t.left(45)
#call draw_spiral function with two distinct turtles
draw_spiral(t1)
draw_spiral(t2)
