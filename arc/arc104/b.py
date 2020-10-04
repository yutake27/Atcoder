n, s = input().split()
n = int(n)

ans = 0

for i in range(n):
    ca = 0
    ct = 0
    cg = 0
    cc = 0
    for j in range(i, n):
        if s[j] == 'A': ca += 1
        elif s[j] == 'T': ct += 1
        elif s[j] == 'G': cg += 1
        elif s[j] == 'C': cc += 1

        if ca == ct and cg == cc:
            ans += 1

print(ans)