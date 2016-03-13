from collections import defaultdict
import re

molecules = set()
rules = defaultdict(list)
base = ""

def readInputFromFile(file):
    global base
    global rules
    for line in file:
        line = line.strip()
        if " => " in line:
            i,o = line.split(" => ")
            rules[i].append(o)
        elif line != "":
            base = line


def addNewMolecules(key, mapList):
    global base
    global molecules
    for m in re.finditer(key, base):
        for replacement in mapList:
            prefix = base[:m.start()]
            suffix = base[m.end():]
            molecules.add(prefix + replacement + suffix)

        
def addAllNewMolecules(rules):
    for key in rules:
        addNewMolecules(key, rules[key])
        
    

f = open('day19-input.txt', 'r')
readInputFromFile(f)
addAllNewMolecules(rules)

print("Part One:",len(molecules))
