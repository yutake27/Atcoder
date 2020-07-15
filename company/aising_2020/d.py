N = int(input())
X = int(input(),2)

def popcount(n):
    return bin(n).count('1')


def f(n):
    if n== 0:
        return 1
    count = 1
    while n!=0:
        n = n%popcount(n)
        count += 1
    return count


X_popcount = popcount(X)
X_mod_p = X%(X_popcount+1)
if X_popcount != 1:
    X_mod_m = X%(X_popcount-1)
for i in range(N):
    X_i = X ^ (1<<(N-i-1))
    if X_i == 0:
        ans = 0
    elif X>>(N-i-1)&1 == 1:
        if X_popcount == 1:
            ans = 1
        else:
            ans = f((X_mod_m-pow(2, N-i-1, X_popcount-1))%(X_popcount-1))
    else:
        ans = f((X_mod_p+pow(2, N-i-1, X_popcount+1))%(X_popcount+1))
    print(ans)