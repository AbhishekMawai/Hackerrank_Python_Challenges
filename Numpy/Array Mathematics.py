import numpy

n, m = map(int, input().split())

A = numpy.array([input().split() for x in range(n)], int)
B = numpy.array([input().split() for x in range(n)], int)
print(A + B, A - B, A * B, A // B, A % B, A**B, sep='\n')
