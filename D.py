a = raw_input().strip().split(' ')
numColumns = int(a[0])
maxFall = int(a[1])
tempCols = raw_input().strip().split(' ')
cols = []
maxDist = 0

for val in tempCols:
	cols.append(int(val))
# print(cols)

lastIndex = 0
for i in range(0,len(cols)):
	if i>= lastIndex:
		tempNum = 1
		for i in range(i,len(cols)):
			if(i+1<len(cols) and abs(cols[i] - cols[i+1]) <= maxFall):
				tempNum += 1
			else:
				lastIndex = i+1
				break

			# print(tempNum, cols[i], cols[i + 1])
		if tempNum > maxDist:
			maxDist = tempNum
		# print(tempNum,maxDist)
print(maxDist)
'''
10 2
1 2 3 10 5 6 7 8 9 10
'''

