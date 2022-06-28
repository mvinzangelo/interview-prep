# 1.3 Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

# ** if you wanted to do this in place in python, start by changing the string to a list since strings are immutable in python.
#    then, start from the back and move to the front, since you don't have to worry about what you're replacing this way

def URLify(string, trueLength):
    URL = ""
    for i in range(0, trueLength):
        if string[i] == ' ':
            URL += "%20"
        else:
            URL += string[i]
    return URL

print((URLify("what up ", 8)))
