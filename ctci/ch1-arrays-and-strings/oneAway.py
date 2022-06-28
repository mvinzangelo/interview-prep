#1.5 There are three types of edits that can be performed on strings: insert, remove, or replace a char. Given two strings, write a function to check if they are one edit away.

def oneAway(stringOne, stringTwo):
    if stringOne == stringTwo:
        return True
    freq = {}
    for i in stringOne:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    for j in stringTwo:
        if j in freq:
            freq[j] = freq[j] - 1
            if freq[j] == 0:
                del freq[j]
        else:
            freq[j] = 1
    if len(stringOne) == len(stringTwo):
        return len(freq) == 2
    else:
        return len(freq) == 1

print(oneAway("pale", "pa"))
