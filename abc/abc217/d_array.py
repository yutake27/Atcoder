import bisect
import array

l, q = map(int, input().split())

cut_list = array.array('i', [0, l])
for _ in range(q):
    l, q = map(int, input().split())
    idx = bisect.bisect(cut_list, q)
    if l == 1:
        cut_list.insert(idx, q)
    elif l == 2:
        print(cut_list[idx] - cut_list[idx - 1])
