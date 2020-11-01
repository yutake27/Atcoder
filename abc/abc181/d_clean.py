s = input()

if len(s) <= 2:
    if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

from collections import Counter
s_counter = Counter(s)

for i in range(100, 1000):
    if i % 8 == 0:
        i_counter = Counter(str(i))
        # Counterは引き算ができるらしい！
        if not i_counter - s_counter:
            print('Yes')
            exit()
print('No')