pf=[]
n=10000000000
for i in range(2,int((n)**1/2)):
	if(n%i==0):
		pf.append(i)
		n=n/i
if(i>n):
	print(pf[-1])
