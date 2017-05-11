n = int(input())
alph = list("abcdefghijklmnopqrstuvwxyz")
cent = "-".join(alph[n - 1:0:-1] + alph[0:1] + alph[1:n])
for i in range(n - 1, -1, -1):
    x = "-".join(alph[i:n])
    print((x[len(x):0:-1] + x).center((len(cent)), "-"))
for j in range(1, n):
    x = "-".join(alph[j:n])
    print((x[len(x):0:-1] + x).center((len(cent)), "-"))
