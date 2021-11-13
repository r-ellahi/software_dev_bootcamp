# # LISTS 1
# import random
# teamA = []
# teamB = []
# players = ["Spinelli", "Gretchen", "Mickey", "T.J.", "Gus", "Vince"]

# while len(players)>0:
#     teamA.append(players.pop(random.randint(0, (len(players)-1))))
#     teamB.append(players.pop(random.randint(0, (len(players)-1))))    

# print(teamA)
# print(teamB)

# # LISTS 2
# my_list = ['apple', 'banana', 'pear']
# my_string = 'fig'

# for item in my_list:
# 	print(item)
	
# for item in my_string:
# 	print(item)

# # LISTS 3
# topic = "slicing strings"

# print(topic[:3])
# print(topic[5:])
# print(topic[2:12])

# # LISTS 4 
# teams = ["WOLVES", "OWLS", "PANTHERS", "BEARS", "DRAGONS"]
# teams_short = []

# for team in teams:
#     teams_short.append(team[:3])

# print(teams_short)

# # LISTS 4
# players = ["Spinelli", "Gretchen", "Mickey", "T.J.", "Gus", "Vince"]
# player_short = []

# for i in players:
#     player_short.append(i[:3])

# print(player_short)


# # LISTS 5: Counting repeated items - PSEUDOCODE FOLLOWED BY WORKING CODE

# # PSEUDOCODE:

# count <- 0

# FOR item <- 0 to LEN(drinks)
#   IF item = “Tea” THEN
#     count <- count + 1
# ENDFOR

# OUTPUT(count)


# # WORKING CODE:

# drinks = ["Tea", "Coffee", "Tea", "Tea", "Coffee", "Hot Chocolate", "Tea"]

# # Dictionary count of all drinks
# result = dict((i, drinks.count(i)) for i in drinks)
# print(result)

# # Count occurrence of repeated element within list 
# repeated_tea = drinks.count("Tea")
# print(repeated_tea)


# # LISTS 6.A
# from random import randint

# scores = []

# for x in range (0, 30):
#     # ^ number of learners (30)
#     scores.append(randint(0, 10))      # Generates a random number from 0 to 10 and append to scores
#     # ^ learner score between 0 - 10
#     tens = 0    # Initialise a variable for counting scores of ten
#     for score in scores:
#         if score == 10:
#             tens += 1
#             print("{0} learners got top marks".format(tens))


# # LISTS 6.b
# import random

# scores = []

# def count(score, scores):
#     count = 0
#     for mark in scores:
#         if mark == score:
#             count += 1
#             return count

# for x in range (0, 30):
#     scores.append(random.randint(0, 10))

# print(scores)

# top_scorers = count(10, scores) # Count function called here

# print("{0} learners got top marks".format(top_scorers))


# # LISTS 6.c
import matplotlib.pyplot as plot

performance = [2,0,2,3,2,4,5,3,2,4,3]

plot.bar(range(11), performance, align='center', alpha=0.5)

plot.xticks(range(11))
plot.ylabel('Score frequency')
plot.title('Scores on a quiz')

plot.show()
plot.savefig(fname="Quiz Chart.png")