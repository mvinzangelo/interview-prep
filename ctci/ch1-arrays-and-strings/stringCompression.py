# 1.6 Implement a method to perform basic string compression using the counts of repeated characters. You can assume the string has only uppercase and lowercase letters.

def stringCompression(inputString):
	buildString = list()
	numRepeated = 1
	for i in range(0, len(inputString) - 1):
		if inputString[i+1] != inputString[i] or i == len(inputString) - 2:
			buildString.append(inputString[i]) 
			buildString.append(str(numRepeated)) 
			numRepeated = 1
		elif inputString[i+1] == inputString[i]:
			numRepeated+= 1
	if len(buildString) >= len(inputString):
		return inputString
	else:
		return ''.join(buildString)
print(stringCompression("aabcccccaaa"))
