# 1.2 Given two strings, write a method to decide if one is a permutation of the other.

def checkPerm(stringOne, stringTwo):
    hashOne = 0
    for i in stringOne:
        hashOne += ord(i)
    hashTwo = 0
    for j in stringTwo:
        hashTwo += ord(j)
    return hashOne == hashTwo

print(checkPerm("hello", "helo"))
