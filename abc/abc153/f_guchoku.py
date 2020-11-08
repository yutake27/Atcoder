n, d, a = map(int, input().split())
xh_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
x_list, h_list = [list(i) for i in zip(*xh_list)]


def search_left(left, h_list):
    for i in range(left, n):
        if h_list[i] > 0:
            return i
    return -1

def search_right(left, right, x_list):
    right = max(left, right)
    for i in range(right, n):
        if x_list[i] > x_list[left] + 2 * d:
            return i - 1
    return n - 1

count = 0
left = 0
right = 0
while True:
    left = search_left(left, h_list)
    if left < 0:
        break
    right = search_right(left, right, x_list)
    c = (h_list[left] - 1) // a + 1
    tmp_left = right
    for i in range(left, right + 1):
        h_list[i] -= c * a
        if h_list[i] > 0:
            tmp_left = min(tmp_left, i)
    left = max(left + 1, tmp_left)
    count += c

print(count)