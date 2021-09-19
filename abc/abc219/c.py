x = input()
n = int(input())
S = [input() for _ in range(n)]
a_ord = ord('a')
x_dict = {c: chr(a_ord + i) for i, c in enumerate(x)}

s_converted_list = []
for i, s in enumerate(S):
    c_list = [x_dict[c] for c in list(s)]
    s_converted = ''.join(c_list)
    s_converted_list.append((s_converted, i))

for name, i in sorted(s_converted_list):
    print(S[i])
