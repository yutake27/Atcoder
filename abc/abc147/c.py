N = int(input())

A_list = []
for i in range(N):
    A = int(input())
    A_list.append([list(map(int, input().split())) for _ in range(A)])


def judge(mask):
    for i in range(N):
        if (mask>>i & 1)==0:
            continue
        for xy in A_list[i]:
            x = xy[0]-1
            y = xy[1]
            if y==0 and (mask>>x & 1):
                return False
            if y==1 and (mask>>x & 1)==0:
                return False
    return True


num_max = 0
for mask in range(1<<N):
    if judge(mask):
        num = 0
        for i in range(N):
            num += mask>>i & 1
        num_max = max(num, num_max)

print(num_max)