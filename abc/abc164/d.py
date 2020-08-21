s = input()
len_s = len(s)
s_array = [int(i) for i in s]

mod = 2019
mod_array = [0]*mod

num = 0
mod_array[0] += 1
for i in range(len_s):
    num = pow(10, i, mod) * s_array[len_s - i - 1] + num
    num %= mod
    mod_array[num] += 1

ans = 0
for i in mod_array:
    ans += (i * (i - 1)) / 2

print(int(ans))