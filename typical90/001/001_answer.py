n, l = map(int, input().split())
k = int(input())
a_list = list(map(int, input().split()))
a_list.append(l)

eql_length = l // (k + 1)


def can_divide(length):
    """length以上の長さで割り切れるかどうかを判定
    """
    ki = 0
    before_ai = 0
    for a in a_list:
        if a - before_ai >= length:
            before_ai = a
            ki += 1
    if ki >= k + 1:
        return True
    else:
        return False


def binary_search(low, high):
    """low以上，high以下の範囲で二分探索 (lowは条件を満たし，highは条件を満たさない)
    """
    while True:
        mid = (low + high) // 2
        if low == mid:
            return low
        canDivide = can_divide(length=mid)
        if canDivide:
            low = mid
        else:
            high = mid


ans = binary_search(0, eql_length + 1)
print(ans)
