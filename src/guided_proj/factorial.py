## call itself
## call with each number, then -1 and multiply it to previous until we hit base case

# Execute
def factorial(n):
### return if we are at n == 1
    if n == 1:
        return 1

## move towards base case
## call itself
## call with each number -1 until hit base case
    return n * factorial(n-1)

# simple tests, true if pass
print(factorial(3) == 6)
print(factorial(4) == 24)

## ** Review **
### Time complexity?
### Space complexity?

# ================================
# Iterative solution

## **Plan**
### Go from 1->n or 1->n


def iter_factorial(n):
### make a tracker: total
    total = 1
###



