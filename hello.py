a=['a', 'b']
b=['abc']
print(a+b)

def factorial(a):
    if a==1:
        return 1
    else:
        result=a*factorial(a-1)
        return result
print(factorial(4))
