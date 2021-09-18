# 問題
https://atcoder.jp/contests/typical90/tasks/typical90_z
![](https://pbs.twimg.com/media/E0A8fQrVcAUrRdt?format=jpg&name=large)

## 案
dfsで端っこを探して，端から奇数ステップで行けるところと，偶数ステップで行けるところを分割

偶数ステップだけで行けるところを最後に出力

### 結果
いくつかのケースでWA

偶数ステップで行けるところが常に過半数以上あるわけではない．

奇数ステップで行ける方が過半数を占めている場合もある．

なので長さを判定してから出力しなければいけない．

## 解説
![](https://pbs.twimg.com/media/E0GHFxrVcAEgtDa?format=jpg&name=large)
