from math import ceil
import numpy as np
import time

# Input Parameters
A=[1,2,3,3,4,5,5,6,7,8,8,8,8,8,8,8,9,9,9,9,9]
x=8

# Numpy based random array
# A=np.random.randint(10,size=(1000000))
# A=np.sort(A)
# x=5

# Algorithm starts from here
def binary_search_leftmost_index(A,x):
    # Only applies to a list of numerical elements sorted in the ascending order.
    mid=0   # Initializing the mid element's index to 0
    index_value=0 # Initializing the index value of the search element to 0. 
    while len(A)!=0:
        mid=ceil((0+(len(A)-1))/2)
        if x!=A[mid]:
            if len(A)==1:
                break
            if x<A[mid]:
                A=A[0:mid+1]
            elif x>A[mid]:
                index_value=index_value+mid
                A=A[mid:]
        elif x==A[mid]:
            if len(A)==2 or len(A)==1:
                index_value=index_value+mid
                print("Element found! Index value: "+str(index_value))
                break
            else:
                A=A[0:mid+1]

start=time.perf_counter()
binary_search_leftmost_index(A,x)
end=time.perf_counter()
print("Time Taken (in seconds): "+str(end-start))
