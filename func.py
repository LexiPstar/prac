from functools import reduce
from pydoc import text

import user
from user import User


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

this = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kos = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if this in kos:
    if this == kos:
        m = this + 1
        kos.append(m)
print(kos)


def comsec():
    name = User.name
    age = User.age
    tel = User.tel
    email = User.email


if __name__ == '__main__':
