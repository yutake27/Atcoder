n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

print(sum([abs(ai - bi) for ai, bi in zip(a, b)]))
