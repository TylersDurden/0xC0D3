from functools import reduce
L = [0, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
m = list(map(lambda x: x**2, L))
r = reduce(lambda x, y:x+y, m)
print r
