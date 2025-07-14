a = []
for i in range(10):
    x = int(input("Enter a number: "))
    a.append(x)
print(a)

minElements = []
maxElements = []

for i in range(3):
    minn = min(a)
    minElements.append(minn)
    a.remove(minn)
    
for i in range(3):
    maxx = max(a)
    maxElements.append(maxx)
    a.remove(maxx)

print(minElements)
print(maxElements)