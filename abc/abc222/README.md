# ABC222
https://atcoder.jp/contests/abc222

久しぶりにリアルタイムで参加した

10分遅れぐらいになってしまった．

a,b,c,dの4問ACで2200位くらい

## C問題
問題が長くて複雑そうだったが解いてみるとそうでもない．

まず勝利数が高い順，次に番号が若い順にソートする．

勝利数を負の数で保存するとソートが楽．


## D問題
DP + 累積和のような感じ．

遷移が少し複雑で実装に手間取った．


## E問題
https://atcoder.jp/contests/abc222/tasks/abc222_e
### 方針
1. まず各辺を通る回数を数えるのが良さそう．

    頂点間を移動する回数Mは多くても100回なので，全てDFSしても計算量的にはいけそう．

2. 次に赤辺と青辺のトータルの数はN-1で固定なので，赤辺の数rtを固定してシミュレーション
   
    rtを固定すると青辺の数btも定まる．

    この時にR-B=kとなるような赤辺，青辺の数が何通りあるかを計算する．

    この計算をどうするかが問題

### 解説
途中までの方針はあっている．

通過する辺の合計数をSとするとR+B=Sで，R-B=kの条件からR=(S+k)/2と求めることができる．

後は，赤辺をRとする通り数を数える．

これはDPを行うとできる．

DFSに更にDPを組み合わせるという発想がなかった．

DPで計算をするという方針が分かれば，自分で実装することができた．

後はS+K<0の場合などの細かい場合を見落とさないようにする．
