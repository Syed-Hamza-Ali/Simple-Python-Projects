#BLACKJACK

logo = """
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |
      `------'                           |__/
"""

def winner(user,computer):
    if user_sum==21 and 11 in user:
        return "You won With a black jack"
    elif comp_sum==21 and 11 in user:
        return "Computer won by Blackjack"
    elif user>21:
        return "You exceeded ..lost"
    elif user > computer:
        return "You win"
    elif user==computer:
        return "Draw"
    else:
        return "You loose"

def aces(user):
    if 'a' in user:
        asked=input("how do you want to proceed\n1\n11\n\n")
        ace=user.index('a')
        if asked=='1':
            user[ace]=1
        elif asked=='11':
            user[ace]=11
        print(user)


from atexit import _clear
import random
_clear()
print(logo)
cards=['a',2,3,4,5,6,7,8,9,10,10,10,10]
cardc=[2,3,4,5,6,7,8,9,10,10,10,10]

user=[]

for i in range(2):
    user.append(random.choice(cards))

print(user)
aces(user)
comp=[random.choice(cardc)]
print(comp)
comp.append(random.choice(cardc))
ask=input("Do you want another card\nyes\nno\n\n")

if ask=='yes':
    user.append(random.choice(cards))
    aces(user)

user_sum=sum(user)
comp_sum=sum(comp)

print(winner(user_sum,comp_sum))
print(f"\nYour Score {user_sum}")
print(f"\nComputer score {comp_sum}")