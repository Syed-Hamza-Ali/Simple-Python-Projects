#Seperate names with ","

import random
names = input('Enter the names')
name = names.split(",")
print(f"{random.choice(name)} will pay the bill")