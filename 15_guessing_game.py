#NUMBER GUESSING GAME
logo="""
   _____                                             _   _                       _
  / ____|                                  /\       | \ | |                     | |
 | |  __   _   _    ___   ___   ___       /  \      |  \| |  _   _   _ __ ___   | |__     ___   _ __
 | | |_ | | | | |  / _ \ / __| / __|     / /\ \     | . ` | | | | | | '_ ` _ \  | '_ \   / _ \ | '__|
 | |__| | | |_| | |  __/ \__ \ \__ \    / ____ \    | |\  | | |_| | | | | | | | | |_) | |  __/ | |
  \_____|  \__,_|  \___| |___/ |___/   /_/    \_\   |_| \_|  \__,_| |_| |_| |_| |_.__/   \___| |_|
"""
import random
print(logo)
guess=random.randint(1,100)
level=input("How do you want to procees \n1)Easy\n2)Hard")
if level=='1':
    turns=10
elif level=='2':
    turns=5
attempts=0
flag=0
for i in range(turns):
    user=int(input("Guess a number"))
    if user<guess:
        print("Guess higher")
    elif user>guess:
        print("Guess lower")
    attempts+=1
    if user==guess:
        print("Found")
        flag=1
        break
if flag==0:
    print("Out of turns\nYou loose")
elif flag==1:
    print(f"You won\nNumber of attempts {attempts}")
