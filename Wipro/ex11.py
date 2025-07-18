'''
['hi',' ','students',' ','bye']
'''

s = ['hi',' ','students','  ','bye']
res = [i for i in s if(lambda x: x!=" ")(i)]
print(res)