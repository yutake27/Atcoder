import numpy as np

n = int(input())
x_list = np.array(list(map(int, input().split())))
tmp = [abs(i) for i in x_list]

man = sum(tmp)
yu = np.sqrt(np.sum(x_list * x_list))
ti = max(tmp)

print(man)
print(yu)
print(ti)