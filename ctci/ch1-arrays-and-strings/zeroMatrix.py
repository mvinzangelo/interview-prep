# 1.8 Write an algorithm such that if a n element in an M x N matrix is 0, its entire row and column are set to 0.

def zeroMatrix(inMatrix):
	zeros = set()
	for i in range(len(inMatrix)):
		for j in range(len(inMatrix[0])):
			if inMatrix[i][j] == 0:
				zeros.add((i,j))

	for k in zeros:
		for x in range(len(inMatrix)):
			inMatrix[x][k[1]] = 0
		for y in range(len(inMatrix[0])):
			inMatrix[k[0]][y] = 0
	print(inMatrix)
	

zeroMatrix([[0,2],[0,5],[7,8]])

