import numpy as np

s = input()
t = input()

len_s = len(s)
len_t = len(t)

ma = 0
for i in range(len_s - len_t + 1):
    ma = max(ma, np.sum(np.array(list(s[i: i + len_t])) == np.array(list(t))))

ans = len_t - ma

print(ans)

