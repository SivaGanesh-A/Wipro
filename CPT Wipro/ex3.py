try:
    file = open("File1.txt")
    str1 = file.readline()
    str2 = file.readline()
    print(str1,str2)
except IOError:
    print("Error is occuringd during input take")
else:
    print("Successfully fetched the data")
