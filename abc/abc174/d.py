n = int(input())
c_array = list(input())

w_num = c_array.count('W')
r_num = n-w_num
def get_ans(half):
    wl_num = c_array[:half].count('W')
    rr_num = c_array[half:].count('R')
    ans = min(wl_num, rr_num) + abs(wl_num-rr_num)
    return ans

ans = min(get_ans(r_num), w_num, r_num)
print(ans)