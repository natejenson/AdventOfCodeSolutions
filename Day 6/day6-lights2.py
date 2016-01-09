##--- Part Two ---
##
##You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.
##
##The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.
##
##The phrase turn on actually means that you should increase the brightness of those lights by 1.
##
##The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.
##
##The phrase toggle actually means that you should increase the brightness of those lights by 2.
##
##What is the total brightness of all lights combined after following Santa's instructions?
##
##For example:
##
##turn on 0,0 through 0,0 would increase the total brightness by 1.
##toggle 0,0 through 999,999 would increase the total brightness by 2000000.


def changeBrightness(lights, start, end, brightness):
    startx,starty = start
    endx,endy = end
    for i in range (startx, endx + 1):
        for j in range (starty, endy + 1):
            lights[i][j] += brightness
            lights[i][j] = max(0,lights[i][j])

def countBrightness(lights):
    count = 0
    for i in range (len(lights)):
        for j in range (len(lights[0])):
            count += lights[i][j]
    return count

def lightshow(inputFile):
    lights = [[0 for i in range(1000)] for j in range(1000)]
    for line in inputFile:
        lineParts = line.split(" ")
        action = lineParts[-4]
        startx,starty = [int(x) for x in lineParts[-3].split(",")]
        endx,endy = [int(x) for x in lineParts[-1].split(",")]

        if(action == "off"):
            changeBrightness(lights,(startx,starty),(endx,endy), -1)
        elif(action == "on"):
            changeBrightness(lights,(startx,starty),(endx,endy), 1)
        elif(action == "toggle"):
            changeBrightness(lights,(startx,starty),(endx,endy), 2)
        else:
            Exception("Action not defined: " + action)
    return countBrightness(lights)

f = open('day6-input.txt','r')

print("lights on:", lightshow(f))
