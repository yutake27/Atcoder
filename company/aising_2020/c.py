N = int(input())


for i in range(1, N+1):
    sum = 0

    range_x = int((i-5)**0.5)+1 if i-5 >0 else 0
    s = set()
    for x in range(1, range_x):
        flag = False
        if x in s:
            continue
        range_y = int((i-x**2-x-3)**0.5)+1 if i-x**2-2*x-2 > 0 else 0
        for y in range(x, range_y):
            if y in s:
                continue
            D = (x+y)**2-4*(x*x+y*y+x*y-i)
            if D >0:
                z = (-(x+y)+D**0.5)/2
                # print(z)
                if z//1 == z and 1<=z:
                    z = int(z)
                    num = len(set([x,y,z]))
                    sum += 6 if num == 3 else 3 if num==2 else 1
                    s = s | set([x,y,z])
                    break

    print(sum)