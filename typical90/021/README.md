# 問題
https://atcoder.jp/contests/typical90/tasks/typical90_u
![](https://pbs.twimg.com/media/EziC-VaUcAY4LmH?format=jpg&name=large)

有向グラフの問題

## 案
単純に頂点の組み合わせ全てに対してDFSやらなんやらでたどり着けるか判定するのでは，計算量的にダメ．

解決策思い付かず．

## 解説
これは強連結成分分解(SCC)という典型らしい．

![](https://pbs.twimg.com/media/EznMbz6VoAAHJ4D?format=jpg&name=large)

強連結成分分解を理解するにはDFSの帰りがけ順を理解している必要がある．

これはDFSをしている際にあるノードから移動可能なノードがなくなった時に，番号をメモするというもの．

末端のノードほど，番号が若くなる．

これによってどこのノードがトップかがわかる．

ここでグラフの向きを真反対にしたときのグラフを考えると，元のグラフでトップのノードは真逆のグラフでは末端のノードである．

真逆のグラフにおいて末端のノードから到達可能な点を求めると，その部分は互いに行き来が可能ということがわかる．

これを繰り返して互いに行き来が可能な部分を求めていくことができる．

## 参考

SCCの考え方
* https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html

pythonでの実装
* https://tjkendev.github.io/procon-library/python/graph/scc.html

    帰りがけ順を保存するために配列にノード番号をappendしていくというのが簡単でよい．



## 再帰のメモ
この問題は再帰を使って解くことができる．

しかしpythonでは再帰回数に上限が定められており，デフォルトの値ではREが出てしまった．

今回は最大でノードの数だけ，再帰をする可能性があるのでノードの数を再帰回数の上限に設定したところ，ACだった．

```python
import sys
sys.setrecursionlimit(100000)
```
