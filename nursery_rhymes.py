def nursery_rhyme():
    answer = int(input("Which nursery rhyme would you like to read? "
                    "1. Itsy Bitsy Spider "
                    "2. Twinkle Twinkle Little Star "
                    "3. Hickory, Dickory, Dock "
                    "4. The ABC Song "))
    if answer == 1:
        print("The itsy bitsy spider crawled up the water spout.",
                "Down came the rain, and washed the spider out.",
                "Out came the sun, and dried up all the rain,"
                "and the itsy bitsy spider went up the spout again")
    elif answer == 2:
        print("Twinkle, twinkle, little star,"
                "How I wonder what you are."
                "Up above the world so high,"
                "Like a diamond in the sky.")
    elif answer == 3:
        print("Hickory, dickory, dock,"
                "The mouse ran up the clock."
                "The clock struck one,"
                "The mouse ran down,"
                "Hickory, dickory, dock")
    elif answer == 4:
        print("A-B-C-D-E-F-G"
                "H-I-J-K-LMNOP"
                "Q-R-S"
                "T-U-V"
                "W and X"
                "Y and Zee"
                "Now I know my 'ABCs'"
                "Next time will you sing with me?")
    else:
        print("Sorry, that selection is invalid, please try again")
        
nursery_rhyme()