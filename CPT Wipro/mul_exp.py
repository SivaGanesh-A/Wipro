# try:
#     num = int(input("Enter a number: "))
#     print(num * 4)
# except KeyboardInterrupt:
#     print("Number should not be entered")
# except TypeError:
#     print("Please check before you enter the datatype")
# except ValueError:
#     print("Please check the value before you enter")

try:
    num = int(input("Enter a number : "))
    print(num * 4)
except (KeyboardInterrupt, ValueError,TypeError):
    print("Number should be enterd .....Program Terminated!!!")
print("bye")