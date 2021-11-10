def nursery_rhyme():
    answer = int(input("""
                    \033[96m\n\tWhich nursery rhyme would you like to read?\033[0m
                    [1] - Itsy Bitsy Spider 
                    [2] - Twinkle Twinkle Little Star 
                    [3] - Hickory, Dickory, Dock 
                    [4] - The ABC Song 
                    """))
    if answer == 1:
        print("""
                The itsy bitsy spider crawled up the water spout.
                Down came the rain, and washed the spider out.
                Out came the sun, and dried up all the rain,
                and the itsy bitsy spider went up the spout again""")
    elif answer == 2:
        print("""
                Twinkle, twinkle, little star,
                How I wonder what you are.
                Up above the world so high,
                Like a diamond in the sky.""")
    elif answer == 3:
        print("""
                Hickory, dickory, dock,
                The mouse ran up the clock.
                The clock struck one,
                The mouse ran down,
                Hickory, dickory, dock""")
    elif answer == 4:
        print("""
                A-B-C-D-E-F-G
                H-I-J-K-LMNOP
                Q-R-S
                T-U-V
                W and X
                Y and Zee
                Now I know my 'ABCs'
                Next time will you sing with me?""")
    else:
        print("Sorry, that selection is invalid, please try again")
        
nursery_rhyme()

# Challenge 2: Create a function with one parameter, name, which will be the name of a person. 
# The function should then “sing” Happy Birthday to that person, inserting their name at the correct point. 
# Give your function a sensible name.


# Challenge 3: Can you make a function which generates a random password of any length? 
# the function should accept one parameter, the desired password length, and return a password. 
# You may find it useful to import the choice function from the random module.