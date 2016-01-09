##--- Day 4: The Ideal Stocking Stuffer ---
##
##Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.
##
##To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.
##
##For example:
##
##If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
##If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
##Your puzzle input is yzbqklnj.
##
##
## PART TWO
## Now find one that starts with six zeroes.

inputStr = "yzbqklnj"

import hashlib
def lowestHash(inputStr, numZeros):
    i = 0
    matchStr = "0"*numZeros
    while True:
        m = hashlib.md5((inputStr+str(i)).encode('utf-8'))
        d = m.hexdigest()
        if(d[:numZeros] == matchStr):
            return i
        i +=1

print("5 zero prefix:", lowestHash(inputStr, 5))
print("6 zero prefix:", lowestHash(inputStr, 6))

