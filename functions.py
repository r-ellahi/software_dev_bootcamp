#Create a haiku function, which prints out each line of a haiku one by one.
def haiku():
    import time
    print("I am very tired,")
    time.sleep(1.0)
    print("But still I code even though,")
    time.sleep(1.0)
    print("I am very tired")
    
haiku()

# Create a function that asks the user for the height and base of a triangle, 
# and then calculates and prints out its area.
def triangle():
    height = float(input("What is the height of the triangle? "))
    base = float(input("What is the base of the triangle? "))
    area = (height * base) / 2
    print(area)

triangle()

# Create function that simulates a coin flip. 
# Each time the function is called, it should randomly select either heads or tails and print it out
def coin_flip():
    import random
    import time
    flip = random.randint(0,1)
    
    guess = input("Heads or Tails? ")
    
    time.sleep(1.5)
    if flip == 0:
        print("Heads, well done!")
    elif flip == 1:
        print("Tails")
    else:
        print("Error, please try again")

coin_flip()


# Create a function that accepts a string and returns the same string reversed.
def reverse():
    answer = input("What word would you like to reverse? ")
    txt = answer[::-1]
    return("Your word reversed is: " + txt)

print(reverse())

# Create a function that simulates a pair of dice being rolled n times
# and returns the number of occurrences of each score.
def dice_roll(n):
    import random
    dice1 = 0
    dice2 = 0
    occurrence = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(0, n):
        dice1 = random.randrange(1, 7)
        if dice1 in occurrence:
            occurrence[dice1] +=1
        dice2 = random.randrange(1, 7)
        if dice2 in occurrence:
            occurrence[dice2] +=1
    return occurrence
        
print(dice_roll(1))

# TURTLE 1
from turtle import Turtle 
tina = Turtle()

def draw_circle(name, r, color, x, y):
    name.penup()
    name.goto(x, y)
    name.dot(2 * r)
    name.color(color)
    

draw_circle(tina, 20, "pink", 20, 20)
#First line of code ^ prints as black on  console - not sure if its an issue with console or code
# remainder of code prints in colours listed except for last line 
draw_circle(tina, 40, "orange", -100, -100)
draw_circle(tina, 60, "yellow", -200, -200)
draw_circle(tina, 40, "lime", 250, 200)



#TURTLE 2
from turtle import Turtle 
tina = Turtle()

def circle_area(r):
    return 3.14 * r * r

def circle_circumference(r):
    return 2 * 3.14 * r 
    

def draw_circle(name, r, color):
    name.color(color)
    name.dot(2 * r)
    
    name.color("black")
    name.goto(0,5)
    name.write("area: " + str(circle_area(r)), align="center")
    name.goto(0, -5)
    name.write("circ: " + str(circle_circumference(r)))
    name.hideturtle()

draw_circle(tina, 100, "blue")


import turtle

def cross():
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)

cross()

def tip(total, percentage):
    new_total = total / 100
    return (new_total * percentage)

print(tip(100, 25))

def dog_years(name, age):
  return (name + " you are " + str(age *7) + " years old in dog years")

print(dog_years("eggs", 3))


def lots_of_math(a, b, c, d):
    first = a + b
    second = c - d
    third = first * second
    fourth = third % a
    print(first)
    print(second)
    print(third)
    return fourth

print(lots_of_math(1, 2, 3, 4))