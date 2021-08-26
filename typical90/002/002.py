n = int(input())

if (n + 1) % 2 == 0:
    exit()


def rec(s, n, num_l, i):
    """Generate () strings

    Args:
        s : Strings
        n : length
        num_l : number of the "("
        i : index
    """
    if i == n and num_l == 0:
        print(s)
    if i == n:
        return
    rec(s + '(', n, num_l + 1, i + 1)
    if num_l > 0:
        rec(s + ')', n, num_l - 1, i + 1)


rec(s='', n=n, num_l=0, i=0)
