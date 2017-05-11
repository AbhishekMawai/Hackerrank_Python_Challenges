N=int(input())
for i in range(1,N+1):
    print(str(i).rjust(len(bin(N)[2:])),oct(i)[2:].rjust(len(bin(N)[2:])),hex(i)[2:].upper().rjust(len(bin(N)[2:])),bin(i)[2:].rjust(len(bin(N)[2:])))