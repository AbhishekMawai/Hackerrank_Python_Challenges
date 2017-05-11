N = input()
M = int(input())
censor = []
out = []
for step in range(0, len(N), M):
    for letter in N[step:step + M]:
        if letter not in censor:
            censor.append(letter)
    news = "".join(censor)
    censor[:] = []
    out.append(news)
for _ in out:
    print(_)
