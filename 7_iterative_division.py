# Solution to problem 6 of the assignment sheet

# Sub question 1

# Declaring our a and b which are the input values
a=147
b=2

# Since division is repeated subtraction, we shall be subtracting b from a repeatedly until b > a
# The quotient can be then be interpreted as to the number of times b can be subtracted from while b <= a.
# When b > a, a can be intepreted as the remainder as a cannot be further subtracted by b.
def iterative_division(a,b):
    quotient=0
    while a>=b:
        a=a-b
        quotient+=1
    return quotient, a

q,r=iterative_division(a,b)

print('Quotient: '+str(q))
print('Remainder: '+str(r))

# Sub question 2
