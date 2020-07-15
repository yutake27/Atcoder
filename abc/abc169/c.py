inp = input().split()

A = int(inp[0])
B=''
for b in inp[1]:
    if b!='.':
        B+=b
B=int(B)


ans_mat_100 = str(A*B)
if len(ans_mat_100)<3:
    print(0)
else:
    print(int(str(A*B)[:-2]))
