##--- Day 11: Corporate Policy ---
##
##Santa's previous password expired, and he needs help choosing a new one.
##
##To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.
##
##Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.
##
##Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:
##
##Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
##Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
##Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
##For example:
##
##hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
##abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
##abbcegjk fails the third requirement, because it only has one double letter (bb).
##The next password after abcdefgh is abcdffaa.
##The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
##Given Santa's current password (your puzzle input), what should his next password be?
##
##Your puzzle input is hxbxwxba.
##
##--- Part Two ---
##
##Santa's password expired again. What's the next one?
##
##Your puzzle input is still hxbxwxba.

import string
import re

# Increments a word (string) and returns the result
def incrementWord(word):
    letters = list(word)
    for i in range(len(letters) -1, -1, -1):
        currentLetter = letters[i]
        newLetter = incrementLetter(currentLetter)
        letters[i] = newLetter
        if(i != 0 and newLetter != "a"):
            break
    return ''.join(letters)

# Increments a single letter and returns the result.
def incrementLetter(letter):
    currentIndex = string.ascii_lowercase.find(letter)
    return string.ascii_lowercase[(currentIndex + 1) % 26]

# Returns True if the given word has n letters in a row.
def hasNLettersInARow(word, n):
    numInRow = 0
    lastLetter = None
    for c in word:
        if (lastLetter == None or ord(c) == ord(lastLetter) + 1):
            numInRow += 1
            if(numInRow == n):
                return True
        else:
            numInRow = 1
        lastLetter = c
    return False

def hasGoodLetters(word):
    return re.search('[ilo]', word) == None

# Returns True if the word contains n non-overlapping repeated sets of characters.
def hasNRepeats(word, n):
    return n == len(re.findall(r'(\w)\1', word))
    
def isValidPassword(password):
    return hasGoodLetters(password) and hasNRepeats(password, 2) and hasNLettersInARow(password, 3)

def getNextPassword(oldPassword):
    nextPassword = oldPassword
    while(True):
        nextPassword = incrementWord(nextPassword)
        if(isValidPassword(nextPassword)):
            return nextPassword
        if (nextPassword == oldPassword):
            Exception("No next password found!")  


oldPassword = "hxbxwxba"

nextPassword = getNextPassword(oldPassword)
print("Part One:", nextPassword)
print("Part Two:", getNextPassword(nextPassword))
    
