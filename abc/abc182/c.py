N = input()

n_sum = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
for n in N:
    n_sum += int(n)
    if int(n) % 3 == 0:
        cnt3 += 1
    elif int(n) % 3 == 1:
        cnt1 += 1
    else:
        cnt2 += 1

ans = 0
if n_sum % 3 == 0:
    print(0)
elif n_sum % 3 == 1:
    if cnt1 > 0 and len(N) > 1:
        print(1)
    elif cnt2 > 1 and len(N) > 2:
        print(2)
    else:
        print(-1)
elif n_sum % 3 == 2:
    if cnt2 > 0 and len(N) > 1:
        print(1)
    elif cnt1 > 1 and len(N) > 2:
        print(2)
    else:
        print(-1)