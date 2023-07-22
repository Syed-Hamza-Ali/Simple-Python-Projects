# Strong Password Creation
import random

num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
alpha = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's',
         'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
anum = ['!', '@', '$', '%', '^', '&', '*']

no_num = int(input("How many numbers you want to be in there : "))
no_alpha = int(input("How many Alphabets you want there : "))
no_anum = int(input("How manny special characters you want : "))

pas = [num, alpha, anum]
pasword = []

for i in range(0, no_num):
    pasword.append(random.choice(num))

for i in range(0, no_alpha):
    pasword.append(random.choice(alpha))

for i in range(0, no_anum):
    pasword.append(random.choice(anum))

random.shuffle(pasword)
password = "".join(pasword)

print("Your password is : ",password)