c = int(input("Enter the temparature in c: "))
f = (c*9/5) + 32
assert(f <= 32), "Its cold"
print("Fahrenheit: ",f)