k = int(input())

def rec(d, n, array):
    array.append(n)

    if d == 10:
        return
    
    for i in [-1, 0, 1]:
        add = n % 10 + i
        if 0 <= add <= 9:
            rec(d + 1, 10 * n + add, array)


array = []
for i in range(1, 10):
    rec(1, i, array)

s_array = sorted(array)
ans = s_array[k - 1]
print(ans)
