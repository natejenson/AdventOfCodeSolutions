##--- Day 6: Probably a Fire Hazard ---
##
##Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.
##
##Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.
##
##Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.
##
##To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.
##
##For example:
##
##turn on 0,0 through 999,999 would turn on (or leave on) every light.
##toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
##turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
##After following the instructions, how many lights are lit?

def offOn(lights, start, end, turnOn):
    startx,starty = start
    endx,endy = end
    for i in range (startx, endx + 1):
        for j in range (starty, endy + 1):
            lights[i][j] = turnOn

def toggle(lights, start,end):
    startx,starty = start
    endx,endy = end
    for i in range (startx, endx + 1):
        for j in range (starty, endy + 1):
            lights[i][j] = not lights[i][j]
    return

def countOn(lights):
    count = 0
    for i in range (len(lights)):
        for j in range (len(lights[0])):
            if (lights[i][j]):
                count += 1
    return count

def lightshow(inputFile):
    lights = [[False for i in range(1000)] for j in range(1000)]
    for line in inputFile:
        lineParts = line.split(" ")
        action = lineParts[-4]
        startx,starty = [int(x) for x in lineParts[-3].split(",")]
        endx,endy = [int(x) for x in lineParts[-1].split(",")]

        if(action == "off"):
            offOn(lights,(startx,starty),(endx,endy), False)
        elif(action == "on"):
            offOn(lights,(startx,starty),(endx,endy), True)
        elif(action == "toggle"):
            toggle(lights,(startx,starty),(endx,endy))
        else:
            Exception("Action not defined: " + action)
    return countOn(lights)

f = open('day6-input.txt','r')

print("lights on:", lightshow(f))

