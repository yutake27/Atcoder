S = input()

day = 0
max_day = 0
for s in S:
    if s == 'R':
        day += 1
        max_day = max(day, max_day)
    else:
        day = 0

print(max_day)