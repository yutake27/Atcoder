import math
k = int(input())

# mod_set = set()
seq = 7

ans = -1
for i in range(k):
    mod = seq%k
    if mod == 0:
        ans = i+1
        break
    # elif seq in mod_set:
        # break
    # mod_set.add(seq)
    seq = mod*10 + 7

print(ans)
