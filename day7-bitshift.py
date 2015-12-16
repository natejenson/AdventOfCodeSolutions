##--- Day 7: Some Assembly Required ---
##
##This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.
##
##Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.
##
##The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.
##
##For example:
##
##123 -> x means that the signal 123 is provided to wire x.
##x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
##p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
##NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
##Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.
##
##For example, here is a simple circuit:
##
##123 -> x
##456 -> y
##x AND y -> d
##x OR y -> e
##x LSHIFT 2 -> f
##y RSHIFT 2 -> g
##NOT x -> h
##NOT y -> i
##After it is run, these are the signals on the wires:
##
##d: 72
##e: 507
##f: 492
##g: 114
##h: 65412
##i: 65079
##x: 123
##y: 456
##In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

# a map of string->string, where the key is the wire,
#and the value is the string operation that computes its value, or the wires integer value, if already computed.
wires = {}

# Parse the input once and build up the associations between the gates.
def buildWiring(inputFile):
    for line in inputFile:
        lhs, rhs = [x.strip() for x in line.split("->")]
        wires[rhs] = lhs.split(" ")

# Do recursion because recursion
def getValue(key):
    # if the value is a number, return it.
    if(key.isdigit()):
        return int(key)

    # if the value has been computed before, return it. This improves performance.
    try:
        return int(wires[key])
    except:
        pass

    # the value of the wire is a yet unevalutated expression. Determine the operator
    # and operands and evaluate/store it.
    opParts = wires[key]
    
    if(len(opParts) == 1):
        op = opParts[0]
        value = getValue(op)
    else:
        operator = opParts[-2]
        if(operator == "AND"):
            op1,op2 = opParts[0],opParts[2]
            value = getValue(op1) & getValue(op2)
        elif(operator == "OR"):
            op1,op2 = opParts[0],opParts[2]
            value = getValue(op1) | getValue(op2)
        elif(operator == "LSHIFT"):
            op1,op2 = opParts[0],opParts[2]
            value = getValue(op1) << getValue(op2)
        elif(operator == "RSHIFT"):
            op1,op2 = opParts[0],opParts[2]
            value = getValue(op1) >> getValue(op2)
        elif(operator == "NOT"):
            op1 = opParts[1]
            value = ~getValue(op1)
    wires[key] = value

    return int(wires[key])
    

def getValueFromFile(f,key):
    buildWiring(f)
    return getValue(key)

f = open('day7-input.txt','r')
print("Wire a: ", getValueFromFile(f,"a"))
