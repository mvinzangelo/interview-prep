def isUnique(string):
    myset = set()
    for i in range(0, len(string)):
        myset.add(string[i])
    return len(myset) == len(string)

print(isUnique("helo"))

