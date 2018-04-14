import random

def InsertionSort(A,N):
    for j in range(1,N):
        key=A[j]
        i=j-1
        while i>=0 and A[i]>key:
            A[i+1]=A[i]
            i=i-1
        A[i+1]=key

    return A

A=[]
S=random.randint(5,10)
for i in range(0,S):
    b=random.randint(0,1000)
    A.append(b)
print(A)
print(InsertionSort(A,len(A)))
