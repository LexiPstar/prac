from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
l = []
for i in r:
    l.append(i)
print(l)


def fn(x, y):
    return x * 10 + y


reduce(fn, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
if this in kos:
