#! python3
# dice.py -- a simple dice rolling game.


import random
import pyinputplus as pyip
from collections import Counter


while True:
    diceSides = pyip.inputNum("How many sides on the dice?\n")
    totalDice = pyip.inputNum("How many dice to roll?\n")

    results = []

    for dice in range(totalDice):                               # roll the dice
        results.append(random.randint(1, diceSides))

    results.sort()

    print("\nYou rolled ...")
    for r in results:
        print(r)                                                # print individual results
    print(f"Total: {sum(results)}")                             # print sum of all results
    for i in range(diceSides):
        count = Counter(results)
        if count[i + 1]:                                        # if a result occurred...
            print(f"{i + 1} occurred {count[i + 1]} times.")    # print count of each result

    repeat = pyip.inputYesNo("Roll again?")
    if repeat == "no":
        break

print("\nGoodbye.")