import math

t = int(input())
l, x, y = map(int, input().split())
q = int(input())


def getEcoord(e):
    ex = 0
    ey = - l * math.sin(2 * math.pi * e / t) / 2
    ez = l / 2 - l * math.cos(2 * math.pi * e / t) / 2
    return (ex, ey, ez)


def getDepressAngle(ex, ey, ez, x, y):
    dist = math.sqrt(x ** 2 + (y - ey) ** 2 + ez ** 2)
    rad = math.asin(ez / dist)
    return math.degrees(rad)


def solve(e):
    ex, ey, ez = getEcoord(e)
    angle = getDepressAngle(ex, ey, ez, x, y)
    print(angle)


for _ in range(q):
    e = int(input())
    solve(e)
