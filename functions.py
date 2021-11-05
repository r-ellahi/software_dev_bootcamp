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
    