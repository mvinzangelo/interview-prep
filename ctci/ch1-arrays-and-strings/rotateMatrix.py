# 1.7 Given an image represented by a N x N matrix, where each pixel in the image is represented by an integer, write a method to rotate the image by 90 degreees. Can you do this in place?


# BRUTE FORCE: O(n^2) space and time
# def rotateMatrix(inMatrix):
# 	outMatrix = [[0] * len(inMatrix) for i in range (len(inMatrix))]
# 	for i in range(0, len(inMatrix)):
# 		for j in range(0, len(inMatrix)):
# 			outMatrix[j][len(inMatrix) - i - 1] = inMatrix[i][j]
# 	return outMatrix

def rotate(inMatrix):
	tempVals = [0] * 4
	for i in range(0, int(len(inMatrix) / 2)):
		tempVals[0] = inMatrix[0][i]
		tempVals[1] = inMatrix[i][len(inMatrix) - 1] 
		tempVals[2] = inMatrix[len(inMatrix) - 1][i] 
		tempVals[3] = inMatrix[len(inMatrix) - 1][len(inMatrix) - 1 - i]
		print(tempVals)
		
		inMatrix[0][i] = tempVals[2]
		inMatrix[i][len(inMatrix) - 1] = tempVals[0]
		inMatrix[len(inMatrix) - 1][i] = tempVals[3]
		inMatrix[len(inMatrix) - 1][len(inMatrix) - 1 - i] = tempVals[1]

	return inMatrix
	

print(rotate([[1,2],[3,4]]))
