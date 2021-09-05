n = int(input())
p = list(map(int, input().split()))

pi = [(p, i + 1) for i, p in enumerate(p)]
pi_sorted = sorted(pi)
ans = [i for p, i in pi_sorted]
print(*ans)
