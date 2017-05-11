N = input()
vowel = ["A", "E", "I", "O", "U"]
stuart, kevin, i = 0, 0, 0
for letter in N:
    if letter not in vowel:
        stuart += len(N) - i
    else:
        kevin += len(N) - i
    i = i + 1
if stuart > kevin:
    print("Stuart", stuart)
elif kevin > stuart:
    print("Kevin", kevin)
else:
    print("Draw")
