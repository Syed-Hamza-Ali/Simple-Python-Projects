# Rock Paper Sciceors
import random

def rock():
    return '''  _______
           - --'   ____)
                 (_____)
                (_____)
                (____)
        ---.__(___)'''

def paper():
    return '''    _______
               ---'   ____)____
                         ______)
                         _______)
                       _______)
              ---.__________)
'''

def secieor():
    return '''    _______
              ---'   ____)____
                        ______)
                    __________)
                  (____)
            ---.__(___)'''

def winer(user, computer):
    if user == 1 and computer == 3:
        return "You Win"
    elif user == 3 and computer == 1:
        return "You loose"
    elif user == computer:
        return "Tied"
    elif user > computer:
        return "You win"
    elif user < computer:
        return "You loost"

print("Rock Paper Scicors")
you = int(input("Select your move\n1)Rock\n2)Paper\n3)Scicors \n\n"))
com = [rock(), paper(), secieor()]
comp = random.randint(0, 2)

if you == 1:
    print(rock())
    print(com[comp])
    print(winer(you, comp+1))

elif you == 2:
    print(paper())
    print(com[comp])
    print(winer(you, comp+1))

elif you == 3:
    print(secieor())
    print(com[comp])
    print(winer(you, comp+1))
