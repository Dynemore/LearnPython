# squares.map.py
# If you code like this you are not a Python dev! ;)
_ = list
squares = []
for n in range(10):
    squares.append(n ** 2)
...
squares
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# This is better, one line, nice and readable
squares = map(lambda n: n**2, range(10))
print(_(squares))
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]