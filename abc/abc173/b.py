import numpy as np

N = int(input())
s = np.array([input() for _ in range(N)])
print('AC x {}'.format(np.count_nonzero(s=='AC')))
print('WA x {}'.format(np.count_nonzero(s=='WA')))
print('TLE x {}'.format(np.count_nonzero(s=='TLE')))
print('RE x {}'.format(np.count_nonzero(s=='RE')))
