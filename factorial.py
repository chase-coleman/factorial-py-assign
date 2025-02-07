# factorials cant be negative or zero
def factorial(n):
    if n < 0: return "Factorials can only be positive integers!"
    sum = 1
    for i in range(n, 0, -1):
        sum = sum * i
    return sum

print(factorial(1)) # == 1
print(factorial(4)) # == 24
print(factorial(10)) # == 362800
print(factorial(0)) # == 1
print(factorial(-1)) # "Factorials can only be positive integers"