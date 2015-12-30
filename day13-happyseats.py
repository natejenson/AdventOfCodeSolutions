##--- Day 13: Knights of the Dinner Table ---
##
##In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.
##
##You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.
##
##For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:
##
##Alice would gain 54 happiness units by sitting next to Bob.
##Alice would lose 79 happiness units by sitting next to Carol.
##Alice would lose 2 happiness units by sitting next to David.
##Bob would gain 83 happiness units by sitting next to Alice.
##Bob would lose 7 happiness units by sitting next to Carol.
##Bob would lose 63 happiness units by sitting next to David.
##Carol would lose 62 happiness units by sitting next to Alice.
##Carol would gain 60 happiness units by sitting next to Bob.
##Carol would gain 55 happiness units by sitting next to David.
##David would gain 46 happiness units by sitting next to Alice.
##David would lose 7 happiness units by sitting next to Bob.
##David would gain 41 happiness units by sitting next to Carol.
##Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.
##
##If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:
##
##     +41 +46
##+55   David    -2
##Carol       Alice
##+60    Bob    +54
##     -7  +83
##After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.
##
####What is the total change in happiness for the optimal seating arrangement of the actual guest list?
##
##--- Part Two ---
##
##In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.
##
##So, add yourself to the list, and give all happiness relationships that involve you a score of 0.
##
##What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
import itertools
from collections import defaultdict

def createHappyMap(happinessMappings):
    happyMap = defaultdict(dict)
    for line in happinessMappings:
        lineParts = line.split()
        person, happiness, neighbor = lineParts[0], int(lineParts[3]), lineParts[-1].strip('.')
        if(lineParts[2] == 'lose'):
            happiness *= -1
        happyMap[person][neighbor] = happiness
    return happyMap

# Get the happiness score for a particular seating alignment.
def getHappinessScore(happyMap, alignment):
    score = 0
    numPeople = len(alignment)
    for i in range(numPeople):
        person = alignment[i]
        leftNeighbor = alignment[i-1]
        rightNeighbor = alignment[(i+1) % numPeople]
        score += happyMap[person][leftNeighbor]
        score += happyMap[person][rightNeighbor]
    return score

# Get the highest happiness score for all seating permutations.
def getBestHappinessScore(happyMap):
    people = list(happyMap.keys())
    highestScore = float('-inf')
    for alignment in itertools.permutations(people):
        alignmentScore = getHappinessScore(happyMap,alignment)
        highestScore = max(highestScore,alignmentScore)
    return highestScore

# For part Two, add a person to the map that has zero effect on the happiness.
def addApatheticPersonToMap(name, happyMap):
    existingPeople = list(happyMap.keys())
    for person in existingPeople:
        happyMap[person][name] = 0
        happyMap[name][person] = 0

f = open('day13-input.txt', 'r')

happyMap = createHappyMap(f.readlines())
bestHappinessScore = getBestHappinessScore(happyMap)
print("Part One:", bestHappinessScore)

addApatheticPersonToMap("Nate", happyMap)
bestHappinessScoreTwo = getBestHappinessScore(happyMap)
print("Part Two:", bestHappinessScoreTwo)


