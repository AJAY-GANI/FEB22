n=int(input('enter the value : '))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(j,end=' ')
	print()
for k in range(1,n+1):
	for l in range(1,n-k+1):
		print(l,end=' ')
	print()