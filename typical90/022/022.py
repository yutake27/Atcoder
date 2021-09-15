import math

a, b, c = map(int, input().split())
ab_gcd = math.gcd(a, b)
ac_gcd = math.gcd(a, c)
abc_gcd = math.gcd(ab_gcd, ac_gcd)
ans = a // abc_gcd + b // abc_gcd + c // abc_gcd - 3
print(ans)
