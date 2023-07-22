#Treasure Hunter


print("Welcome to the Treasure hunting ")
direction = input("Which way you want to proceed\nLeft\nRight\n\n")
direction.lower()
if direction == 'left':
    print("Oh shit !! It's a mud monster.\n Ahhhghghhg........\n You died Game Over")
elif direction == 'right':
    print("Well! it looks like you are in your second stage")
    direction = input(
        'you have reached at lake\n1)You wanna Swim\n2)You wanna wait for the boat\n\n')
    if direction == '1':
        print("Damn there are crocodials\n krab krab kraaaab....\n you died Game over")
    elif direction == '2':
        direction = input("""\nrYou'r going well\n\nOh you have reached at the doors of fate
        From here either you will find the Treasure or you wil die
        Select the door
        1)RED
        2)BLUE
        3)BLACK
        """)
        if direction == '3':
            print('''
*******************************************************************************
          | | | |
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
        else:
            print("You Died")
