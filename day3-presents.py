##--- Day 3: Perfectly Spherical Houses in a Vacuum ---
##
##Santa is delivering presents to an infinite two-dimensional grid of houses.
##
##He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
##
##However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
##
##For example:
##
##> delivers presents to 2 houses: one at the starting location, and one to the east.
##^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
##^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
##
##--- Part Two ---
##
##The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.
##
##Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.
##
##This year, how many houses receive at least one present?
##
##For example:
##
##^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
##^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
##^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
##
def housesHit(inputStr):
    houses = set((0,0))
    x=y= 0
    for c in inputStr:
        if(c == '^'):
            y += 1
        elif(c == 'v'):
            y -= 1
        elif(c == '>'):
            x += 1
        elif(c == '<'):
            x -= 1

        houses.add((x,y))
    return len(houses)

###
### Part Two Solution
###
def twoSantas(inputStr):
    houses = set([(0,0)])
    x=y=0   # Santa's Coords
    x2=y2=0 # RobotSanta's Coords
    
    switch = True
    for c in inputStr:
        if(switch):
            x,y = switchHouse(houses, (x,y), c)
        else:
            x2,y2 = switchHouse(houses, (x2,y2), c)
        switch = not switch
    return len(houses)

# Move from currCoods to a new house in the house map, direction determined by nextDir
# houses: set of (x,y), currCoords: (x,y) tuple, nextDir: string '>'
#   returns new coordinates
def switchHouse(houses, currCoords, nextDir):
    x,y = currCoords
    if(nextDir == '^'):
        y += 1
    elif(nextDir == 'v'):
        y -= 1
    elif(nextDir == '>'):
        x += 1
    elif(nextDir == '<'):
        x -= 1
    houses.add((x,y))
    return (x,y)

f = open('day3-input.txt','r')
inputStr = f.read()
print("One Santa:", housesHit(inputStr))
print("Two Santas:", twoSantas(inputStr))

