N = int(input())
A = sorted(list(map(int, input().split())))
# print(A)

table = [0]*N

for i in range(N):
    for j in range(i+2):
        # print(i,j)
        if i!=j and A[i]%A[j]==0:
            table[i]=1
            break
        if A[i]/2 <= A[j]:
            if i == (N-1):
                if A[i-1] == A[i]:
                    table[i] = 1
            elif A[i] == A[i-1] or A[i] == A[i+1]:
                table[i] = 1
            break

# print(table)
print(table.count(0))
