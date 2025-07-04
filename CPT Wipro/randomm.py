import random
class RandomError(Exception):
    pass
try:
    num = random.random()
    if num < 0.1:
        raise RandomError
except RandomError as e:
    print("RandoError is generated")
else:
    print("%.4f"%num)

    