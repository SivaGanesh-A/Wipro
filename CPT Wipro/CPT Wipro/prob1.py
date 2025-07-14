a = int(input("Enter a number: "))

for i in range(1,a+1):
    print(f"{" "*(a-i)}{int('1'*i)**2}{" "*(a+i)}")
    
    
    
