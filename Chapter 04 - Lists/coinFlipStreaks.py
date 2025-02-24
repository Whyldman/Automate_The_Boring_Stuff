# Create a program to determine the likelihood of a 6 streak of heads or tails in 100 flips

import random
numberOfStreaks = 0

for experimentNumber in range(10000):
    headsOrTails = []
    for coin in range(100):
        headsOrTails.append(random.randint(0,1))

    hasStreak = 0
    for i in range(len(headsOrTails)-6):
        if sum(headsOrTails[i:i+6]) == 6 or sum(headsOrTails[i:i+6]) == 0:
            hasStreak += 1

    if hasStreak > 0:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))