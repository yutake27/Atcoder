import math

A, B, H, M = map(int, input().split())

H_angle = 30*H+0.5*M
M_angle = 6*M

angle = abs(H_angle-M_angle)
angle = min(angle, 360-angle)

ans = (A*A+B*B-2*A*B*math.cos(math.radians(angle)))**0.5
print(ans)
