numStars = int(raw_input())
starsLocs = []
totalDist = 0
dists = []
for i in range(0,numStars):
	temp = raw_input().split(' ')
	starsLocs.append([int(temp[0]),int(temp[1])])
# print(starsLocs)

def calcDist(x1,y1,x2,y2):
	return (abs(x1-x2) + abs(y1-y2))

for i in range(1,len(starsLocs)):
	# print(starsLocs[i])
	# print(i)
	distFromCenter = calcDist(starsLocs[0][0],starsLocs[0][1],starsLocs[i][0],starsLocs[i][1])
	dists.append(distFromCenter)
	totalDist += distFromCenter
print(totalDist)
for val in dists:
	print(val)