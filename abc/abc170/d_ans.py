from collections import Counter
N = int(input())
A = sorted(list(map(int, input().split())))
count = Counter(A)

max_len_A = 10**6+1
data = [0]*max_len_A
A = list(set(A))

for a in A:
    if data[a]==0:
        for j in range(a+a, max_len_A, a):
            data[j]+=1


ans = len([a for a in A if data[a]==0 and count[a]==1])
print(ans)