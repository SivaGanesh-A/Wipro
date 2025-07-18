words = ['shiva','ganesh','meow']

rw = [(lambda w: w[::-1])(word) for word in words]
print(rw)