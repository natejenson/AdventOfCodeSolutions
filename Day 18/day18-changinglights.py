##    --- Day 18: Like a GIF For Your Yard ---
##
##    After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.
##
##    Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.
##
##    Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".
##
##    Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".
##
##    For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:
##
##    1B5...
##    234...
##    ......
##    ..123.
##    ..8A4.
##    ..765.
##    The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:
##
##    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
##    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
##    All of the lights update simultaneously; they all consider the same current state before moving to the next.
##
##    Here's a few steps from an example configuration of another 6x6 grid:
##
##    Initial state:
##    .#.#.#
##    ...##.
##    #....#
##    ..#...
##    #.#..#
##    ####..
##
##    After 1 step:
##    ..##..
##    ..##.#
##    ...##.
##    ......
##    #.....
##    #.##..
##
##    After 2 steps:
##    ..###.
##    ......
##    ..###.
##    ......
##    .#....
##    .#....
##
##    After 3 steps:
##    ...#..
##    ......
##    ...#..
##    ..##..
##    ......
##    ......
##
##    After 4 steps:
##    ......
##    ......
##    ..##..
##    ..##..
##    ......
##    ......
##    After 4 steps, this example has four lights on.
##
##    In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

import copy

# Get the initial state of the lights from the input file. Assumes n-by-n grid.
def getInitialLights(file):
    linesInFile = file.readlines()
    inputX,inputY = len(linesInFile[0].strip()), len(linesInFile)
    lights = [[False for i in range(inputX)] for j in range(inputY)]
    for y in range(inputY):
        for x in range(inputX):
            if(linesInFile[y][x] == "#"):
                lights[y][x] = True
    return lights

# Returns the number of adjacent neighbors that have 'on' lights.
def numNeighborsOn(posX,posY,lights):
    result = 0
    for y in range(posY-1,posY+2):
        for x in range(posX-1,posX+2):
            try:
                # Make sure to skip the orignal light.
                if(x == posX and y == posY):
                    continue

                # If we have negative indices, treat as out of range.
                if(x < 0 or y < 0):
                    raise IndexError()
                
                if(lights[y][x]):
                    result += 1
            except IndexError:
                # If we're out of range, treat the light as 'off'
                continue
    return result

# Animate a light at position (x,y) in the given lights.
def animateLight(x,y,lights):
    lightIsOn = lights[y][x]
    neighborsOn = numNeighborsOn(x,y,lights)

    if(lightIsOn):
        return neighborsOn == 2 or neighborsOn == 3
    else:
        return neighborsOn == 3

# Animate all of the lights in the given two-dimensional array.
def animateLights(lights):
    oldState = copy.deepcopy(lights)
    for y in range(len(oldState)):
        for x in range(len(oldState[0])):
            lights[y][x] = animateLight(x,y,oldState)
    return lights

def animateLightsN(lights, n):
    for i in range(n):
        lights = animateLights(lights)
    return lights

# Counts the number of 'on' lights.
def countLightsOn(lights):
    count = 0
    for y in range(len(lights)):
        for x in range(len(lights[y])):
            if(lights[y][x]):
                count += 1
    return count
            

f = open('day18-input.txt','r')
lights = getInitialLights(f)

print("Part One:", countLightsOn(animateLightsN(lights, 100)))

