n = int(input())
a_list = list(map(int, input().split()))

rui_a = [0] * (n + 1)
rui_max_a = [0] * (n + 1)
rui_ite = [0] * (n + 1)
for i in range(n):
    rui_a[i + 1] = rui_a[i] + a_list[i]
    rui_max_a[i + 1] = max(rui_max_a[i], rui_a[i + 1])
    rui_ite[i + 1] = rui_ite[i] + rui_a[i + 1]

ans = 0
for i in range(1, n + 1):
    ans = max(ans, rui_ite[i - 1] + rui_max_a[i])

print(ans)