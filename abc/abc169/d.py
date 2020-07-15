N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[] and n!=1:
        arr.append([n, 1])

    return arr

arr = factorization(N)


candidate_arr = sorted([arr[i][0]**(j+1) for i in range(len(arr)) for j in range(arr[i][1])])

ans = 0
for c in candidate_arr:
    if N%c==0:
        ans+=1
        N /= c

print(ans)

