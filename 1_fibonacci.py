
# Problem 1: 

# Sub Question 1
n=3 # The number of fibonacci numbers to be printed

def fibonacci(n):
    fib=[]
    f,temp,prev=1,1,1 # Intializing the values temporary value, fibonacci value and the previous fibonacci value to 1.
    for i in range(0,n):
        if i==0 or i==1: # Both of the first 2 elements of the fibonacci sequence are 1 
            fib.append(1)
        else: # Apply the calculation for the fibonacci sequence
            temp=f
            f=temp+prev
            prev=temp
            fib.append(f)
    return fib

f=fibonacci(n)
print(f)

# Sub Question 2
def fibonacci_function_calls(fib):
    last_index=len(fib)-1
    fib_num=0
    count=0
    for i in range(0,len(fib)):
        fib_num=fib[last_index-i]
        if last_index-i-2!=0:
            print()

    # return 0

# function_calls=
# fibonacci_function_calls(f)
# print("Number of Function Calls: "+str(function_calls))
