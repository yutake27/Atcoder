import itertools

n, m, q = map(int, input().split())
abcd_array = [list(map(int, input().split())) for _ in range(q)]

def get_sum(A, abcd_array):
    sum = 0
    for abcd in abcd_array:
        a, b, c, d = abcd
        if A[b-1] - A[a-1] == c:
            sum += d
    return sum

candidate_array = list(itertools.combinations_with_replacement(range(1,m+1), n))
ans = 0
for A in candidate_array:
    ans = max(ans, get_sum(A, abcd_array))

print(ans)