##--- Day 12: JSAbacusFramework.io ---
##
##Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.
##
##They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.
##
##For example:
##
##[1,2,3] and {"a":2,"b":4} both have a sum of 6.
##[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
##{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
##[] and {} both have a sum of 0.
##You will not encounter any strings containing numbers.
##
##What is the sum of all numbers in the document?
##
##--- Part Two ---
##
##Uh oh - the Accounting-Elves have realized that they double-counted everything red.
##
##Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).
##
##[1,2,3] still has a sum of 6.
##[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
##{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
##[1,"red",5] has a sum of 6, because "red" in an array has no effect.

###
### Part One
###
f = open('day12-input.txt','r')
inputString = f.read()

import re
print("Part One:", sum([int(x.strip()) for x in re.findall(r'-?\d+', inputString)]))


###
### Part Two
###
import json
with open('day12-input.txt') as inputFile:    
    inputJson = json.load(inputFile)

# Get the sum of all integers in the json Object without 'reds'
def getSumWithoutReds(jsonObj):
    result = 0
    values = jsonObj
    if (type(jsonObj) is dict):
        values = jsonObj.values()
        if ("red" in values):
            return 0
    for val in values:
        if type(val) is int:
            result += int(val)
        elif type(val) is list or type(val) is dict:
            result += getSumWithoutReds(val)          
    return result

    
print("Part Two:", getSumWithoutReds(inputJson))


