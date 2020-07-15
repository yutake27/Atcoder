n = int(input())
mod = 26

i= 0
name = ''
while n>0:
    n -= 1
    name += chr(ord('a')+n%mod)
    n //= mod


print(name[::-1])