# 問題
https://atcoder.jp/contests/typical90/tasks/typical90_m

![](https://pbs.twimg.com/media/EyzsXh_U8AAJ4IC?format=jpg&name=large)


## 案
最短経路探索を中間地点iごとに行う．

各点ごとに毎回ダイクストラをするのは計算量的に厳しそう．(ダイクストラの計算量はO((n + m)logn))


## 解説
始点からのダイクストラと終点からのダイクストラを足せば良い！
![](https://pbs.twimg.com/media/Ey41_9eVkAIC8lU?format=jpg&name=large)

なるほど！

