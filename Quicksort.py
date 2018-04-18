def Partition(A,p,r):
	x=A[r]
	i=p-1
	for j in range(p,r):
		if A[j]<=x :
			i=i+1
			A[i],A[j]=A[j],A[i]

	A[i+1],A[r]=A[r],A[i+1]

	return i+1

def Quicksort(A,p,r):
	if p<r:
		q=Partition(A,p,r)
		Quicksort(A,p,q-1)
		Quicksort(A,q+1,r)

	return A




A=[2,8,7,1,3,5,6,4,5,6]

print(Quicksort(A,0,9))
