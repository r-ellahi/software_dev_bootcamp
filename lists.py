# # LISTS 1
# import random
# teamA = []
# teamB = []
# players = ["Spinelli", "Gretchen", "Mickey", "T.J.", "Gus", "Vince"]

# while len(players)>0:
#     teamA.append(players.pop(random.randint(0, (len(players)-1))))
#     teamB.append(players.pop(random.randint(0, (len(players)-1))))    

# print(teamA)
# print(teamB

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


# LISTS 5 - PSEUDOCODE FOLLOWED BY WORKING CODE


# PSEUDOCODE:
count <- 0

FOR item <- 0 to LEN(drinks)
  IF item = “Tea” THEN
    count <- count + 1
ENDFOR

OUTPUT(count)


# WORKING CODE:

# drinks = ["Tea", "Coffee", "Tea", "Tea", "Coffee", "Hot Chocolate", "Tea"]
# new_list = []

# for drink in drinks:
#     if drink == "Tea":
#         new_list = new_list +1
# print(int(new_list))


drinks = ["Tea", "Coffee", "Tea", "Tea", "Coffee", "Hot Chocolate", "Tea"]

# Dictionary count of drinks
result = dict((i, drinks.count(i)) for i in drinks)
print(result)

# Count occurrence of repeated element within list 
repeated_tea = drinks.count("Tea")
print(repeated_tea)


