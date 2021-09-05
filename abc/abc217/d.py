import bisect

l, q = map(int, input().split())

cut_list = [0, l]
for _ in range(q):
    l, q = map(int, input().split())
    if l == 1:
        bisect.insort(cut_list, q)
    elif l == 2:
        idx = bisect.bisect(cut_list, q)
        print(cut_list[idx] - cut_list[idx - 1])
