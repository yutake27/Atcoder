# ABC217
https://atcoder.jp/contests/abc217

## A~C
特になし

## D問題
二分探索でいけるかと思ったが，insert時にO(n)かかってしまい，
総計算量がO(n^2)となり1ケースTLEした．

c++などでは順序付き集合という値の挿入もO(logn)でできるものがある．
しかしながらpythonにはないので自分で実装するしかない...

平衡二分木とかを勉強する必要がある．

### arrayを用いた高速化
O(n^2)のはずだが，pythonのarrayを使うと通るらしい．
arrayのinsertが速い？

```python
import bisect
import array

l, q = map(int, input().split())

cut_list = array.array('i', [0, l])
for _ in range(q):
    l, q = map(int, input().split())
    idx = bisect.bisect(cut_list, q)
    if l == 1:
        cut_list.insert(idx, q)
    elif l == 2:
        print(cut_list[idx] - cut_list[idx - 1])
```
numpyでやってみたらダメだった(AtcoderのPyPy3はnumpyが使えないのでPython3で提出した)

## e問題
優先度付きキューと普通のキューの二つを使うところがポイント