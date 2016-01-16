##--- Day 16: Aunt Sue ---
##
##Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".
##
##You have 500 Aunts named "Sue".
##
##So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.
##
##The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:
##
##children, by human DNA age analysis.
##cats. It doesn't differentiate individual breeds.
##Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
##goldfish. No other kinds of fish.
##trees, all in one group.
##cars, presumably by exhaust or gasoline or something.
##perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
##In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:
##
##children: 3
##cats: 7
##samoyeds: 2
##pomeranians: 3
##akitas: 0
##vizslas: 0
##goldfish: 5
##trees: 3
##cars: 2
##perfumes: 1
##You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.
##
##What is the number of the Sue that got you the gift?
##
##--- Part Two ---
##
##As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.
##
##In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).
##
##What is the number of the real Aunt Sue?

MFCSAM = {"children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1}

class Sue:
    def __init__(self, number, things):
        self.number = number
        self.things = things

    def hasThingMatch(self, thing):
        return (thing in self.things) and (self.things[thing] == MFCSAM[thing])

    def hasRangedThingMatch(self, thing):
        if (not thing in self.things):
            return False
        if (thing in ["cats","trees"]):
            return self.things[thing] > MFCSAM[thing]
        if (thing in ["pomeranians","goldfish"]):
            return self.things[thing] < MFCSAM[thing]
        
        return self.things[thing] == MFCSAM[thing]


def getAllTheSues(inputLines):
    sues = []
    for line in inputLines:
        _,number, *things = [part.strip().strip(":").strip(",") for part in line.split()]
        it = iter(things)
        sues.append(Sue(number, dict((k,int(v)) for k,v in zip(it,it))))
    return sues

def findTheRightSue(sues, useRanges=False):
    for sue in sues:
        isMatch = True
        for axiom in MFCSAM.keys():
            # If this sue doesn't have the item, we can't determine her status yet.
            if (not axiom in sue.things):
                continue

            # Determine which function to use to determine a match.
            if (useRanges):
                hasMatchFunc = sue.hasRangedThingMatch
            else:
                hasMatchFunc = sue.hasThingMatch

            # If this isn't the Sue we want, go to the next one.
            if(not hasMatchFunc(axiom)):
                    isMatch = False
                    break;
                
        if (isMatch):
            return sue.number
    return None


f = open('day16-input.txt','r')
sues = getAllTheSues(f.readlines())


print("Part One:", findTheRightSue(sues))
print("Part Two:", findTheRightSue(sues, True))
