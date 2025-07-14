x = int(input("Enter a number: "))

for i in range(x+1):
    print(f"{" "*(x-i)} {'*'*i}")