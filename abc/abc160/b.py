x = int(input())

ans = 0

div_500, x = divmod(x, 500)
div_5, x = divmod(x, 5)

ans = div_500 * 1000 + div_5 * 5
print(ans)