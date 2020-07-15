from functools import reduce
import numpy as np

mod=10**9+7

def mat(list):
    return reduce(lambda a,b: a*b%mod, list)


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
A = np.array(sorted(A, key=abs, reverse=True))
A_pn = A < 0
if N == np.count_nonzero(A_pn):
    if K % 2 == 0:
        print(mat(A[:K]))
    else:
        print(mat(A[-K:]))
elif np.count_nonzero(A_pn[:K]) % 2 == 0:
    print(mat(A[:K]))
elif N==K:
    print(mat(A))
else:
    negative_all = np.where(A_pn)[0]
    negative_rest = np.count_nonzero(negative_all>=K)
    if negative_rest == 0:
        # 負の数が残っていない
        A[negative_all[-1]] = A[K]
        print(mat(A[:K]))
    elif negative_rest == N-K:
        # 正の数が残っていない
        last_positive = np.where(A_pn[:K]==False)[0][-1]
        A[last_positive] = A[K]
        print(mat(A[:K]))
    elif len(negative_all)-negative_rest==K:
        # 負の数しか選択されていない
        last_negative = negative_all[negative_all<K][-1]
        next_positive = np.where(A_pn==False)[0][0]
        A[last_negative] = A[next_positive]
        print(mat(A[:K]))
    else:
        last_negative = negative_all[negative_all<K][-1]
        next_negative = negative_all[negative_all>=K][0]
        positive_all = np.where(A_pn==False)[0]
        last_positive = positive_all[positive_all<K][-1]
        next_positive = positive_all[positive_all>=K][0]
        if A[last_negative]*A[next_negative] > A[last_positive]*A[next_positive]:
            A[last_positive] = A[next_negative]
        else:
            A[last_negative] = A[next_positive]
        print(mat(A[:K]))
