# Hangman

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words = ["syed", "meer", "hamza", "shah",
         "trying", "coding", "instead", "sleeping"]
guess = random.choice(words)
hint = []
for i in guess:
    hint.append(i)
# print(guess)
# print(hint)
disp = list("_"*len(guess))
print(disp)
flag = 0
k = 2
print(stages[6])
end_game = False
while not end_game:

    user = input("Enter the word : ").lower()
    print(user)
    flag2 = 0

    for i in range(0, len(guess)):
        j = guess[i]
        if j == user:
            disp[i] = j
            print(disp)
            flag2 = 1
        if disp == hint:
            flag = 1
            break
    if k == 8:
        break
    if flag2 == 0:
        print(stages[-k])
        k += 1
    if "_" not in disp:
        end_game = True

if flag == 1:
    print("You won")
else:
    print("You are hanged")