# 1.1 Implement an algorithm to determine if a string has all uque characters. What if you can't use additional data structures?
def isUnique(string):
    myset = set()
    for i in range(0, len(string)):
        myset.add(string[i])
    return len(myset) == len(string)

print(isUnique("hello"))


