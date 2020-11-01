import bisect

n, m = map(int, input().split())
h_list = sorted(list(map(int, input().split())))
w_list = sorted(list(map(int, input().split())))

diff_list = [0] * n
diffl_sum_list = [0] * (n // 2 + 1)
diffr_sum_list = [0] * (n // 2 + 1)

for i in range(1, n):
    diff_list[i] = h_list[i] - h_list[i - 1]
    if i % 2:
        diffl_sum_list[i // 2 + 1] = diffl_sum_list[i // 2] + diff_list[i]
    else:
        diffr_sum_list[i // 2] = diffr_sum_list[i // 2 - 1] + diff_list[i]



ans_min = float('inf')
for w in w_list:
    w_where = bisect.bisect_left(h_list, w)
    if w_where % 2:
        pair_sum = diffl_sum_list[w_where // 2] + w - h_list[w_where - 1] + diffr_sum_list[-1] - diffr_sum_list[w_where // 2]
    else:
        pair_sum = diffl_sum_list[w_where // 2] + h_list[w_where] - w + diffr_sum_list[-1] - diffr_sum_list[w_where // 2]
    if pair_sum < ans_min:
        ans_min = pair_sum

print(ans_min)