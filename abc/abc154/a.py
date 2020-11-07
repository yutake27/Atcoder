s, t = input().split()
a, b = map(int, input().split())
u = input()

dic = {s: a, t: b}
dic[u] -= 1

print(dic[s], dic[t])