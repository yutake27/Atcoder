import math
import bisect


def getDeclination(x1, y1, x2, y2):
    # 二つの座標から偏角を求める
    # 戻り値は全て正の度数
    rad = math.atan2(y2 - y1, x2 - x1)
    deg = math.degrees(rad)
    return deg if deg >= 0 else 360 + deg


def getAngle(rad1, rad2):
    # 二つの偏角から角度を求める
    dif = rad2 - rad1
    return dif if dif < 180 else 360 - dif


def solve(n, xy):
    deg = 0
    for i in range(n):  # 各点を中心と固定してループ
        xi, yi = xy[i]  # 中心点
        dec_list = []
        for j in range(n):  # 中心以外の点について中心点との偏角を求める
            if i == j:
                continue
            xj, yj = xy[j]
            dec = getDeclination(xi, yi, xj, yj)
            dec_list.append(dec)
        dec_list.sort()  # 偏角を昇順にソート
        for j in range(n - 1):  # 各偏角についてなす角が最大となるもう一つの偏角を二分探索で求める
            rad1 = dec_list[j]
            rad_best = (rad1 + 180) % 360  # 最適な値
            idx = bisect.bisect(dec_list, rad_best)  # 挿入箇所を二分探索で探索
            rad_cand1 = dec_list[(idx - 1) % len(dec_list)]
            rad_cand2 = dec_list[idx % len(dec_list)]
            deg = max(deg, getAngle(rad1, rad_cand1), getAngle(rad1, rad_cand2))
    return deg


def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    ans = solve(n, xy)
    print(ans)


if __name__ == '__main__':
    main()
