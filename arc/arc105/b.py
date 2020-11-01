n = int(input())
a_list = list(map(int, input().split()))
a_min = min(a_list)

def update(a_list):
    a_min = min(a_list)
    for i, a in enumerate(a_list):
        mod = a % a_min
        if mod == 0:
            a_list[i] = a_min
        else:
            a_list[i] = mod
    return a_list


while True:
    a_list = update(a_list)
    a_max = max(a_list)
    a_min = min(a_list)
    if a_max == a_min:
        break
ans = a_min
print(ans)