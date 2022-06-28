# 1.4 Given a string, write a function to check if it is a permutation of a palindrome.

def palindromePerm(string):
    freq = {}
    isEven = len(string) % 2 == 0
    for i in string:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1
    numEvens = 0
    numOdds = 0
    for j in freq:
        if freq[j] % 2 == 0:
            numEvens += 1
        else:
            numOdds += 1
    if isEven:
        return numOdds == 0
    else:
        return numOdds == 1
    
print(palindromePerm("ooooooxo"))
