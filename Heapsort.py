import random
def MAXHEAPIFY(A,i,s):
	left=2*i+1
	right=2*i+2
	largest=i
	if left<s and A[left]>A[i]:
		largest=left

	if right<s and A[right]>A[largest]:
		largest=right

	if largest !=i:
		a=A[i]
		A[i]=A[largest]
		A[largest]=a
		MAXHEAPIFY(A,largest,s)


def BUILDMAXHEAP(A,s):
	for i in range(0,int(len(A)/2))[::-1]:
		MAXHEAPIFY(A,i,s)
	return A


def Heapsort(A,s):
	BUILDMAXHEAP(A,s)
	for i in range(0,s)[::-1]:
		A[0],A[i]=A[i],A[0]
		s=s-1
		MAXHEAPIFY(A,0,s)

	return A

A=[]
s=random.randint(5,100)
for i in range(0,s):
	A.append(random.randint(0,100))
print(Heapsort(A,s))



