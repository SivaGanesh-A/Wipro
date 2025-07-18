'''
code to decalre the longest string using lambda
'''
long = lambda a,b:a if len(a)<len(b) else b
print(long('shiva','ganesh'))
print(long('1234','11'))
