import numpy

n, m = map(int, input().split())
li = numpy.array([input().split() for x in range(n)], int)
y = numpy.sum(li, axis=0)
print(numpy.prod(y, axis=0))
