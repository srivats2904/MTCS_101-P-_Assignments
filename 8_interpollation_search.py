from math import floor,ceil
import numpy as np
import time

# Input Parameters
A=[1,2,3,3,4,5,5,6,7,8,8,8,8,8,8,8,9,9,9,9,9]
x=9

# Numpy based random array
# A=np.random.randint(10,size=(1000000))
# A=np.sort(A)
# x=5

def interpolation_search(A,x):
    index_value=0
    j=0
    l=0
    u=len(A)-1
    prev_u=0
    while l!=u:
        prev_u=u
        j=ceil(((u*x)-(l*x)-(u*A[l])-(l*A[u]))/(A[u]-A[l]))
        if A[j]!=x:
            if len(A)==1:
                index_value=-1
                break
            if x<A[j]:
                A=A[0:j]
            elif x>A[j]:
                index_value=index_value+j
                A=A[j:]
        elif A[j]==x:
            index_value=index_value+j
            if len(A)==1:
                break
            else:
                A=A[j:]
        u=len(A)-1
        if prev_u==u:
            break
    return index_value

start=time.perf_counter()
i=interpolation_search(A,x)
end=time.perf_counter()
print('Index Value: '+str(i))
print("Time Taken (in seconds): "+str(end-start))

