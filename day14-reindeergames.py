##--- Day 14: Reindeer Olympics ---
##
##This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.
##
##Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.
##
##For example, suppose you have the following Reindeer:
##
##Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
##Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
##After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.
##
##In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).
##
##Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
##
##  Your puzzle answer was 2640.
##
##--- Part Two ---
##
##Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.
##
##Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.
##
##Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.
##
##After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).
##
##Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?
##
##  Your puzzle answer was 1102.

class Reindeer:
    def __init__(self, name, speed, speedTime, restTime):
        self.name = name
        self.speed = speed
        self.speedTime = speedTime
        self.restTime = restTime
        self.points = 0
        self.currentDistance = 0

# Get the distance of the farthest reindeer at the given time.
def farthestDistanceAtTime(allReindeer, time):
    farthestDistance = 0
    for reindeer in allReindeer:
        farthestDistance = max(farthestDistance, distanceAtTime(reindeer,time))
    return farthestDistance

# Start a race and determine the most points received by any reindeer at the given time.
def mostPointsAtTime(allReindeer, time):
    race(allReindeer, time)
    return max([reindeer.points for reindeer in allReindeer])

# Race the reindeer and add points at each time interval.
def race(allReindeer, time):
    for reindeer in allReindeer:
        reindeer.points = 0
    for t in range(1,time + 1):
        for reindeer in allReindeer:
            reindeer.currentDistance = distanceAtTime(reindeer, t)
        addPoints(allReindeer)

# Add points to the reindeer that are in the lead.
def addPoints(allReindeer):
    bestDistance = max([reindeer.currentDistance for reindeer in allReindeer])
    for reindeer in allReindeer:
        if(reindeer.currentDistance == bestDistance):
            reindeer.points += 1

# Get the distance of a reindeer at a certain time.
def distanceAtTime(reindeer, t):
    s = reindeer.speed
    x = reindeer.speedTime
    r = reindeer.restTime
    
    block = t//(x+r)
    isInFlight = (t%(r+x) <= x)
    if(isInFlight):
        timeInFlight = t%(x+r)
        return(s*(timeInFlight + (x*(block))))
    else:
        return(s*x*(1+(block)))

# Read the input file and create our reindeer
def getReindeerFromFile(file):
    reindeerList = []
    for line in file:
        line = line.split()
        reindeerList.append(Reindeer(line[0],int(line[3]),int(line[6]), int(line[-2])))
    return reindeerList

f = open('day14-input.txt','r')
reindeer = getReindeerFromFile(f)

print("Part One:", farthestDistanceAtTime(reindeer,2503))
print("Part Two:", mostPointsAtTime(reindeer,2503))

