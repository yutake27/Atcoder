N = int(input())

k = N%10

if k==3:
    print('bon')
elif k in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')