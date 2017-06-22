import numpy
n, m = map(int, input().split())
li = numpy.array([input().split() for x in range(n)], int)
y = numpy.min(li, axis=1)
print(numpy.max(y, axis=0))
