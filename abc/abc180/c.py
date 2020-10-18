N = int(input())
divisors = []
for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i:
            divisors.append(N//i)

divisors.sort()

for div in divisors:
    print(div)