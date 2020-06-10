# given a and b, return a ** b, without using the inbuilt operator


## Plan
### We have 2 numbers, one or both may be naegative numbers

### Iterative vs. recursive?

def iter_power(a, b):
    # check for exponent  == 0
    if b == 0:
        return 1

    # have a counter
    product = a
    while b!= 1:
        product *= a
        b -= 1

    return product
    






print(iter_power(2, 3) == 2 **3)
print(iter_power(2, 3) == 2 **3)
print(iter_power(2, 3) == 2 **3)
print(iter_power(2, 3) == 2 **3)
print(iter_power(2, 3) == 2 **3)
