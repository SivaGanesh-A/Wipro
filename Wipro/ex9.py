# data = ['pen','cap','bat']
# upper = [(lambda x: x.upper())(d) for d in data]
# print(upper)

'''
word = 'shiva'
op = 'avihs'
'''
word = 'shiva'
a = [(lambda x: x[::-1])(word)]
print(*a)