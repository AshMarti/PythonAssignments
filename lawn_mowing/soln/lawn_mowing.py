#circle cost = 2r
#remaning sections= 4lwi

a=input().split()
l=float(a[0])
w=float(a[1])

totalcost=0
if l<=w: 
	radius=(l/2)
	l=l/2
elif w<l: 
	radius=(w/2)
	w=w/2

circlecost=2*radius
if a[0]==a[1]:
	for i in range(4):
		totalcost+=4*l*l*(i+1) 
else:
	for i in range(2):
		totalcost+=4*l*w*(i+1) 

totalcost+=circlecost
print(int(totalcost))