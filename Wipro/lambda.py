'''
data = [10,'hi',4.5,'students',3,100]
from the list containig numbers and strings,
extract only integers using lambda function
and list comprehensions 

o/p : [10,3,100]
'''

# a = [int(x) for x in data if (lambda s:str(int(s)).isdigit())(x)]
# print(a)

data = [10,'hi',4.5,'students',3,100]
a = [x for x in data if(lambda v:type(v)==int)(x)]
print(a)
