x = lambda num1,num2:num1+num2
#print(x(11,22))

big = lambda x,y: x if x>y else y
#print(big(5,2))

nums = [11,22,33,44,55,77,99]
e = list(filter(lambda num: num%2==0,nums))
print(e)