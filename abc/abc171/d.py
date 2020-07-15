N = int(input())
A = list(map(int, input().split()))
Q = int(input())
bc = [list(map(int, input().split())) for _ in range(Q)]

mem = [0]*(10**5)

sum = 0
for i in A:
    mem[i-1] += 1
    sum += i

for q in range(Q):
    b = bc[q][0]
    if mem[b-1] != 0:
        c = bc[q][1]
        num = mem[b-1]
        mem[c-1] += num
        mem[b-1] = 0
        sum = sum - num*b + num*c
    print(sum)

