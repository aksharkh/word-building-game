from django.shortcuts import render
import random

# Open the dictionary file and read all lines
f1 = open('dictionary.txt', 'r') 
words = []
cmarks = []
umarks = []
temp1 = f1.readlines()

# Prepare the list of words
for i in temp1:
    word1 = i.replace('\n', '')
    words.append(word1)

# Initial computer choice
rand1 = random.randrange(0, len(words))
computerchoice = words[rand1]
print('computer: ', computerchoice)
cmarks.append(len(computerchoice))
words.remove(computerchoice)
lastchar1 = computerchoice[-1]
print(lastchar1)

# Main game loop
while True:
    userchoice = input('user: ')
    if userchoice.startswith(lastchar1) and userchoice in words:
        lastchar2 = userchoice[-1]
        umarks.append(len(userchoice))
        words.remove(userchoice)
        temp2 = list(filter(lambda i: i.startswith(lastchar2), words))
        if not temp2:
            print('user wins')
            break
        rand2 = random.randrange(0, len(temp2))
        computerchoice = temp2[rand2]
        print('computer: ', computerchoice)
        cmarks.append(len(computerchoice))
        lastchar1 = computerchoice[-1]
        words.remove(computerchoice)
    else:
        print('computer wins')
        break

print('computer marks:', sum(cmarks))
print('user marks:', sum(umarks))
