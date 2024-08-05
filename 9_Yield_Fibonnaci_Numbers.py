
n=12 # The number of fibonacci numbers to be printed

def fibonacci(n):
    fib=[]
    f,temp,prev=1,1,1 # Intializing the values temporary value, fibonacci value and the previous fibonacci value to 1.
    for i in range(0,n):
        if i==0 or i==1: # Both of the first 2 elements of the fibonacci sequence are 1 
            yield "1"
        else: # Apply the calculation for the fibonacci sequence
            temp=f
            f=temp+prev
            prev=temp
            yield str(f)
    return fib

f=fibonacci(n)

for i in f:
    print(i)
