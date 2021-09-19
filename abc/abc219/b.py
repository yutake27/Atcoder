s1 = input()
s2 = input()
s3 = input()

S = ''
t = input()
for c in list(t):
    if c == '1':
        S += s1
    elif c == '2':
        S += s2
    elif c == '3':
        S += s3
print(S)
