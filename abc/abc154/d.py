n, k = map(int, input().split())
p_list = list(map(int, input().split()))

rui_sum = [sum(p_list[:k])]
for i in range(1, n - k + 1):
    rui_sum.append(rui_sum[i - 1] + p_list[i + k - 1] - p_list[i - 1])

ans = (max(rui_sum) + k) / 2

print(ans)