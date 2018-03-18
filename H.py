m = raw_input().strip()
b = raw_input().strip().split(' ')
c = []
for code in b:
	c.append(int(code))
c.sort()
# print(c)
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'.split(',')
# print(alphabet)
# '''
# helloaliens
# 2 14 20 10 23 12 22 18 11 19 9 13 25 15 5 7 17 1 4 6 0 24 8 21 16 3
# '''
final = ''
for i in range(0,len(m)):
	index = alphabet.index(m[i])
	final += str(c[index]) + ' '
print(final)
