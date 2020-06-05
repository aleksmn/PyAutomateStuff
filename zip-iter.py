"""
How does zip(*[iter(s)]*n) work in Python?

iter() is an iterator over a sequence. [x] * n produces a list containing
n quantity of x, i.e. a list of length n, where each element is x. *arg
unpacks a sequence into arguments for a function call. Therefore you're
passing the same iterator 3 times to zip(), and it pulls an item from the
iterator each time.

"""

x = iter(range(9))

print (list(zip(*[x] * 3))) # [(0, 1, 2), (3, 4, 5), (6, 7, 8)]


# without iter:


print(list(zip(*[range(9)] * 3))) # [(0, 0, 0), (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5), (6, 6, 6), (7, 7, 7), (8, 8, 8)]
