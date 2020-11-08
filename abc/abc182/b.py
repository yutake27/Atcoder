n = int(input())
a_list = list(map(int, input().split()))

ans = 0
gcd = 0
for b in range(2, 1001):
    tmp_gcd = 0
    for a in a_list:
        if a % b == 0:
            tmp_gcd += 1
    if tmp_gcd > gcd:
        gcd = tmp_gcd
        ans = b

print(ans)