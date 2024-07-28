print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("You are at a crossroads. Do you want to go left or right?")
direction = str.lower(input("Type 'left' or 'right': \n"))
if direction == "left":
          print("You come to a lake. There is an island in the middle of the lake. Do you want to swim or wait for a boat?")
          movement = str.lower(input("Type 'swim' or 'wait': \n"))
          if movement == "wait":
                    print("You have arrived at the island unharmed. There is a house with 3 doors. One red, one yellow")
                    door = str.lower(input("Which door do you choose? Type 'red', 'yellow', or 'blue': \n"))
                    if door == "yellow":
                              print("You win! You found the treasure!")
                    elif door == "red":
                              print("You spontaneously combust. Game over")
                    else:
                              print("You wander into a room full of beasts. Game over.")                       
          else:
                    print("You were attacked by a trout. Game over.")
else:
          print("You fell into a hole. Game over.")
          
          