from datetime import *
d = date.today()
print(d)
d = date(1966, 6, 29)
for x in range(1,10):
    nextdate = d + timedelta(days = x)
    print(nextdate)