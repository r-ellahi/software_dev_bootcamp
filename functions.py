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
