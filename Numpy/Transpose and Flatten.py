import numpy as np
n,m=map(int,input().split())
li=[]
for i in range(n):
    x=list(map(int,input().split()))
    li.append(x)
my_array = np.array(li)
print(np.transpose(my_array))
print(np.ndarray.flatten(my_array))
