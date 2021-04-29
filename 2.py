a=0
b=1
sum=0
while a+b<4000000:
	c=a+b
	a=b
	b=c
	if c%2==0:
		sum+=c
print(sum)
#4613732