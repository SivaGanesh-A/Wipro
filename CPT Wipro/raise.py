try:
    raise NameError
except:
    print("Re-raising the exception")
finally:
    print("///")