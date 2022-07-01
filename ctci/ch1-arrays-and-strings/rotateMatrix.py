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
		for j in range(0, int(len(inMatrix) / 2)):
			tempVals[0] = inMatrix[i][j]
			tempVals[1] = inMatrix[j][len(inMatrix) - 1 - i] 
			tempVals[2] = inMatrix[len(inMatrix) - 1 - j][i] 
			tempVals[3] = inMatrix[len(inMatrix) - 1 - i][len(inMatrix) - 1 - j]
		
		
			inMatrix[i][j] = tempVals[2]
			inMatrix[j][len(inMatrix) - 1 - i] = tempVals[0]
			inMatrix[len(inMatrix) - 1 - j][i] = tempVals[3]
			inMatrix[len(inMatrix) - 1 - i][len(inMatrix) - 1 - j] = tempVals[1]
		
		for j in inMatrix:
			print(j)
		print()	

	return inMatrix
	
rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
# print(rotate([[1,2],[3,4]]))

