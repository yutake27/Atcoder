n, m = map(int, input().split())

updated = [False] * n
number = [0] * n
if n != 1:
    number[0] = 1

flag = True
for i in range(m):
    s, c = map(int, input().split())
    if not updated[s - 1]:
        if not n == 1 and s == 1 and c == 0:
            flag = False
            break
        updated[s - 1] = True
        number[s - 1] = c
    elif updated[s - 1] and number[s - 1] != c:
        flag = False
        break

if flag:
    ans = ''.join(map(str, number))
else:
    ans = -1

print(ans)