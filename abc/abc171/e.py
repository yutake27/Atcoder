from functools import reduce

n = input()
a = list(map(int, input().split()))

s = int(reduce(lambda i,j: i^j, a))
print(' '.join(list(map(lambda x: str(x^s), a))))
