n, k = map(int, input().split())
h_list = sorted(list(map(int, input().split())), reverse=True)

ans = sum(h_list[k:])
print(ans)