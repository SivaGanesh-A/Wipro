'''
calucalate the factorial of n using recursion of lambda
function.

n = 4
'''

fact = (lambda f: lambda n:1 if n==0 else
         n*f(f)(n-1))(lambda f: lambda n:1 
                     if n==0 else n*f(f)(n-1))
print(fact(5))

dsum = (lambda f: lambda n:0 if n==0 else n%10 +f(f)(n//10))
(lambda f:lambda n:0 if n==0 else n%10 +f(f)(n//10))
print(dsum(1234))