n = int(input())
p_list = list(map(int, input().split()))

ans = 0
p_set = set()
for i in range(n):
    p = p_list[i]
    p_set.add(p)
    if ans in p_set:
        while True:
            ans += 1
            if not ans in p_set:
                break
    print(ans)