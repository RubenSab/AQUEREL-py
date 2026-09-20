from src.execution.node import *

a = Node("a", None)
b = Node("b", a)
a.append(b)
c = Node("c", b)
b.append(c)
d = Node("d", c)
c.append(d)

x = Node("x", None)
y = Node("y", x)
x.append(y)
z = Node("z", y)
y.append(z)

# extract(a, b)
# extract(b, c)
# extract(c, d)

# replace(a, x, z); print(x.str_chain())
# replace(d, x, y); print(a.str_chain())
# replace(b, x, z); print(a.str_chain())

# splice_after(d, x, z)

print(a.str_chain())