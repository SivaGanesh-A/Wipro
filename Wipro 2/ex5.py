st = 'aeiou'
s = input("Enter a string: ")
l = ''
for i in s:
    if i.lower() in st:
        l += 'z'
    else:
        l += i   
print(l)


