n = int(input())
a_array = list(map(int, input().split()))

before = 0
sum = 0
for a in a_array:
    if before > a:
        sum += before - a
    else:
        before = a

print(sum)