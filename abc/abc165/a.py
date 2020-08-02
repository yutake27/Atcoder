k = int(input())
a, b = map(int, input().split())

if int((a-1)/k + 1)*k <= b:
    print('OK')
else:
    print('NG')