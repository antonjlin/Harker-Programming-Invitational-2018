
a = raw_input().strip().split(' ')
numPlanets = int(a[0])
numPairs = int(a[1])

distances = [0]
for i in range(1,numPlanets):
	newDist = distances[i-1] + int(raw_input())
	distances.append(newDist)
	# print(newDist)
toFind = []
for i in range(0,numPairs):
	temp = raw_input().split(' ')
	arr = [int(temp[0]) -1,int(temp[1]) -1]
	toFind.append(arr)
# print(distances)
# print(toFind)
for i in range(0,len(toFind)):
	p1Index = toFind[i][0]
	p2Index = toFind[i][1]
	# print(p2Index,p1Index)
	# print(distances[p2Index],distances[p1Index])
	dist = abs((distances[p2Index] - distances[p1Index]))
	print(dist)